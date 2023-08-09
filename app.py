import os

import pandas as pd
from fancyimpute import KNN
from flask import Flask, request, jsonify

app = Flask('spawner')


@app.route('/knn', methods=['POST'])
def knn():
    args = request.args.to_dict(flat=False)
    neighbours = args.get("neighbours", 5)
    impute_columns = args.get("impute_columns", [])
    impute_columns = [eval(i) for i in impute_columns]
    data = request.files.get('file')
    # url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
    data = pd.read_csv(data, header=None)

    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].astype('category')
            data[col] = data[col].cat.codes

    columns = data.columns
    data = data.values

    data_out = KNN(k=neighbours).fit_transform(data)

    data_out = pd.DataFrame(data_out, columns=columns)
    data_out = data_out[[8, 9]]
    data_out = data_out[impute_columns]
    data_dict = dict()
    for col in data_out.columns:
        data_dict[col] = data_out[col].values.tolist()
    jsonify_data = jsonify(data_dict)
    return jsonify_data, 200


if __name__ == '__main__':
    if os.name == 'nt':
        temp_dir = os.environ.get('Temp')
    else:
        temp_dir = '/tmp'
    pid = open(os.path.join(temp_dir, 'scaler_pid.txt'), 'w')
    pid.write(str(os.getpid()))
    pid.close()

    app.run(host='0.0.0.0', port=5353, threaded=True)
