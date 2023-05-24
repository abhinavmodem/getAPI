from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'host': 'abhinavmodem.mysql.pythonanywhere-services.com',
    'user': 'abhinavmodem',
    'password': '@Abhi2004',
    'database': 'abhinavmodem$test'
}

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    if request.method == 'POST':
        new_word = request.form.get('new_word')
        query = 'UPDATE test_table SET test_word = %s;'
        cursor.execute(query, (new_word,))
        conn.commit()
        cursor.close()
        conn.close()
        return 'Word updated successfully'

    query = 'SELECT test_word FROM test_table LIMIT 1;'
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        test_word = result[0]
    else:
        test_word = 'No test word found'

    return render_template('admin.html', test_word=test_word)

if __name__ == '__main__':
    app.run()
