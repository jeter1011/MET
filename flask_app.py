from flask import Flask, render_template, send_file, Response
import pandas as pd
import met_main

app = Flask(__name__, static_folder='static', template_folder='templates')
raw_: list
recipe_name : str

@app.route('/')
def index1():
    print("Index function called")
    return render_template('index1.html')


@app.route('/data')
def data():

    global raw_
    global recipe_name

    print("data function called")
    raw_ = met_main.pull_recipe()
    data_dict = met_main.variables_df.to_dict(orient='records')
    recipe_name = data_dict[0]['Values']
    return render_template('data.html', data=data_dict, recipe=recipe_name)


@app.route('/file_transfer')
def file_transfer():
    return render_template('file_transfer.html', recipe = recipe_name)


@app.route('/download')
def download_file():

    # Save the Raw list as a CSV file
    raw_csv = pd.DataFrame(raw_).to_csv(index=False)

    response = Response(
        raw_csv,
        mimetype='text/csv',
        headers={'Content-Disposition' : f'attachment; filename={recipe_name}.csv',
                 'Content-Type': 'text/csv',
                 'Content-Length': str(len(raw_csv))
                 }
    )

    return response




if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000, debug=True)
