from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'abhinav1',
    'database': 'test'
}
@app.route('/')
def get_test_word():
    # Connect to the MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Retrieve the "Test" word from the database
    query = 'SELECT test_word FROM test_table LIMIT 1;'
    cursor.execute(query)
    result = cursor.fetchone()

    # Close the database connection
    cursor.close()
    conn.close()

    if result:
        return result[0]
    else:
        return 'No test word found'
@app.route('/admin', methods=['GET', 'POST'])
def admin_portal():
    if request.method == 'POST':
        new_word = request.form.get('new_word')

        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Update the "Test" word in the database
        query = 'UPDATE test_table SET test_word = %s;'
        cursor.execute(query, (new_word,))
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        return 'Word updated successfully'

    # Render the admin portal template
    return render_template('admin.html')
if __name__ == '__main__':
    app.run(debug=True)
