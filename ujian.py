from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import random
import datetime
import time
from flask import Markup
from flask import Flask


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ismayakusumah6'
app.config['MYSQL_DB'] = 'qc'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


# home
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home2')
def home2():
    return render_template("home2.html")

# end home

# about
@app.route('/about')
def about():
    return render_template("about.html")
# end about

# login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM user_managemen WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return render_template("home2.html")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")
# end login

# login admin
@app.route('/login2', methods=["GET", "POST"])
def login2():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM user_managemen WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return render_template("home.html")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login2.html")
# end login admin

# register

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
         if request.form['email'] == '':
            flash('Harap Data diisi')
            return render_template("register.html")
         else:
             if request.form['name'] == '':
                flash('Harap Data diisi')
                return render_template("register.html")
             else:
                if request.form['password'] == '':
                    flash('Harap Data diisi')
                    return render_template("register.html")
                else:
                    name = request.form['name']
                    email = request.form['email']
                    password = request.form['password'].encode('utf-8')
                    password = bcrypt.hashpw(password, bcrypt.gensalt())
                    cur = mysql.connection.cursor()
                    cur.execute("INSERT INTO user_managemen (name, email, password) VALUES (%s,%s,%s)",
                                (name, email, password))
                    mysql.connection.commit()
                    session['name'] = request.form['name']
                    session['email'] = request.form['email']
                    return redirect(url_for('home'))

# end register

# register user

@app.route('/register2', methods=["GET", "POST"])
def register2():
    if request.method == 'GET':
        return render_template("register2.html")
    else:
         if request.form['email'] == '':
            flash('Harap Data diisi')
            return render_template("register2.html")
         else:
             if request.form['name'] == '':
                flash('Harap Data diisi')
                return render_template("register2.html")
             else:
                if request.form['password'] == '':
                    flash('Harap Data diisi')
                    return render_template("register2.html")
                else:
                    name = request.form['name']
                    email = request.form['email']
                    password = request.form['password'].encode('utf-8')
                    password = bcrypt.hashpw(password, bcrypt.gensalt())
                    cur = mysql.connection.cursor()
                    cur.execute("INSERT INTO user_managemen (name, email, password) VALUES (%s,%s,%s)",
                                (name, email, password))
                    mysql.connection.commit()
                    session['name'] = request.form['name']
                    session['email'] = request.form['email']
                    return redirect(url_for('home2'))

# end register user

# Logout

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("home.html")

# end Logout


# User Management
@app.route('/user_managemen')
def user_managemen():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user_managemen")
    rv = cur.fetchall()
    cur.close()
    return render_template('user_managemen.html', user_managemens=rv)


@app.route('/simpan-user_managemen', methods=["POST"])
def saveuser_managemen():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user_managemen (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    mysql.connection.commit()
    return redirect(url_for('user_managemen'))


@app.route('/update-user_management', methods=["POST"])
def updateuser_managemen():
    id_data = request.form['id']
    nama = request.form['name']
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE user_managemen SET name=%s, email=%s, password=%s WHERE id=%s", (nama ,email,password,id_data,))
    mysql.connection.commit()
    return redirect(url_for('user_managemen'))

@app.route('/hapus-user_managemen/<string:id_data>', methods=["GET"])
def hapususer_managemen(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM user_managemen WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('user_managemen'))
# end User Management


# Delivery_product
@app.route('/delivery_product')
def delivery_product():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM delivery_product")
    rv = cur.fetchall()
    cur.close()
    return render_template('delivery_product.html',delivery_products=rv)


@app.route('/simpan-product', methods=["POST"])
def savedelivery_product():
    nama = request.form['name']
    tanggal = request.form['date']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO delivery_product (name, date) VALUES (%s, %s)", (nama, tanggal))
    mysql.connection.commit()
    return redirect(url_for('delivery_product'))


@app.route('/update-delivery_product', methods=["POST"])
def updatedelivery_product():
    id_data = request.form['id']
    nama = request.form['name']
    tanggal = request.form['date']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE delivery_product SET name=%s, date=%s WHERE id=%s", (name,date,id_data,))
    mysql.connection.commit()
    return redirect(url_for('delivery_product'))

@app.route('/hapus-delivery_product/<string:id_data>', methods=["GET"])
def hapusdelivery_product(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM delivery_product WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('delivery_product'))
# end delivery_product

# Delivery_product
@app.route('/delivery_product2')
def delivery_product2():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM delivery_product")
    rv = cur.fetchall()
    cur.close()
    return render_template('delivery_product2.html',delivery=rv)
# End Delivery_product


# Validasi_product
@app.route('/validasi_product')
def validasi_product():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM validasi_product")
    rv = cur.fetchall()
    cur.close()
    return render_template('validasi_product.html',validasi_products=rv)


@app.route('/simpan-validasi_product', methods=["POST"])
def savevalidasi_product():
    name = request.form['name']
    date = request.form['date']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO validasi_product (name, date, status) VALUES (%s, %s, %s)", (name, date, status))
    mysql.connection.commit()
    return redirect(url_for('validasi_product'))


@app.route('/update-validasi_product', methods=["POST"])
def updatevalidasi_product():
    id_data = request.form['id']
    name = request.form['name']
    date = request.form['date']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE validasi_product SET name=%s, date=%s, status=%s WHERE id=%s", (name, date, status, id_data,))
    mysql.connection.commit()
    return redirect(url_for('validasi_product'))

@app.route('/hapus-validasi_product/<string:id_data>', methods=["GET"])
def hapusvalidasi_product(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM validasi_product WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('validasi_product'))
# end delivery_product

# Validasi_product
@app.route('/validasi_product2')
def validasi_product2():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM validasi_product")
    rv = cur.fetchall()
    cur.close()
    return render_template('validasi_product2.html',validasi=rv)
# end Validasi_product

# Sparepart
@app.route('/sparepart')
def sparepart():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sparepart")
    list_part = cur.fetchall()
    cur.execute("SELECT status, count(status) as count_status FROM sparepart GROUP BY status")
    status_count = cur.fetchall()

    chart_labels = []
    chart_data = []
    for st in status_count:
        chart_labels.append(str(st['status']))
        chart_data.append(st['count_status'])

    print(chart_labels)

    return render_template('sparepart.html', list_part = list_part, chart_data = chart_data, chart_labels = chart_labels)

@app.route('/add_sparepart', methods=["POST"])
def add_sparepart():
    n = request.form['btnradio']
    converted_num = int(n)
    for i in range(converted_num):
        nama_part = request.form['nama_part']
        numbering = str(i)
        nama = nama_part + numbering
        letters = ['Good', 'Not Good']
        random_index1 = random.choices(letters)
        letter = ['Mobil', 'Sepeda', 'Bajai', 'Motor']
        random_index = random.choices(letter)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sparepart (nama_part, status) VALUES (%s, %s)", (random_index, random_index1))
        mysql.connection.commit()
        time.sleep(10)
    return redirect(url_for('sparepart'))   

@app.route('/edit_sparepart/<id>', methods = ['POST', 'GET'])
def edit_sparepart(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sparepart WHERE Id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('_sparepart.html', data = data[0])


@app.route('/update_sparepart/<Id>', methods=['POST'])
def update_sparepart(Id):
    if request.form['btnradio'] == 'Good':
        cur = mysql.connection.cursor()
        letterz = ['Good']
        cur.execute(" UPDATE sparepart SET status = %s WHERE Id = %s ", (letterz, Id))
        mysql.connection.commit()
        return redirect(url_for('sparepart'))
    if request.form['btnradio'] == 'Not Good':
        cur = mysql.connection.cursor()
        letterz = ['Not Good']
        cur.execute(" UPDATE sparepart SET status = %s WHERE Id = %s", (letterz, Id))
        mysql.connection.commit()
        return redirect(url_for('sparepart'))

@app.route('/delete_sparepart/<string:id_data>', methods=["GET"])
def delete_sparepart(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM sparepart WHERE Id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('sparepart'))

@app.route("/add_chart")
def chart():
    cur = mysql.connection.cursor()
    data_1 = cur.execute('SELECT * FROM sparepart WHERE Id = OK', (id))
    ok_data = data['data_1'].count()
    data_2 = cur.execute('SELECT * FROM sparepart WHERE Id = REJECT', (id))
    reject_data = data['data_2'].count()
    labels = ["OK","REJECT"]
    values = int([ok_data, reject_data])
    return render_template('chart.html', values=values, labels=labels)


# end Sparepart

# Sparepart
@app.route('/sparepart2')
def sparepart2():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sparepart")
    list_part = cur.fetchall()
    cur.execute("SELECT status, count(status) as count_status FROM sparepart GROUP BY status")
    status_count = cur.fetchall()

    chart_labels = []
    chart_data = []
    for st in status_count:
        chart_labels.append(str(st['status']))
        chart_data.append(st['count_status'])

    print(chart_labels)

    return render_template('sparepart2.html', list_part = list_part, chart_data = chart_data, chart_labels = chart_labels)

@app.route('/sparepart_mobile')
def sparepart_mobile():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sparepart")
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    for result in rv:
     return render_template('sparepart_mobile.html', list_part=rv)



if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(host='0.0.0.0', debug=True)
