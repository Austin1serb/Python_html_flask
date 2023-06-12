from flask import Flask, render_template  
app = Flask(__name__)   


@app.route('/play')          
def play():
    num_times = 3
    return render_template('index.html', num_times=num_times) 

@app.route('/play/<x>')
def x_times(x):
    num_times = int(x)
    return render_template('index.html', num_times=num_times)


@app.route('/play/<x>/<color>')
def x_color(x, color):
    num_times = int(x)
    return render_template('index.html', num_times=num_times, color=color)


if __name__=="__main__":  
    app.run(debug=True)  
