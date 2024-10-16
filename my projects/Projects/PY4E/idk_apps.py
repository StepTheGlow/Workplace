# Application 1: Basic Print Statements and Integer Conversion
def app1():
    """
    Prints 'Hello world', calculates 40 / 10, converts 98.6 to an integer, and prints the results.
    """
    print('Hello world')
    print(40 / 10)
    x = int(98.6)
    print(x)

# Application 2: Finding the Smallest Number in a List
def app2():
    """
    Finds the smallest number in a given list and prints it.
    """
    smallest_so_far = None
    for the_num in [9, 41, 12, 3, 74, 15]:
        if smallest_so_far is None or the_num < smallest_so_far:
            smallest_so_far = the_num
    print('Smallest number:', smallest_so_far)

# Application 3: Calculating Average Spam Confidence from a File
def app3():
    """
    Calculates the average spam confidence from a file specified by the user.
    """
    file_name = input("Enter the file name: ")

    count = 0
    total_confidence = 0.0

    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    colon_pos = line.find(':')
                    confidence_str = line[colon_pos + 1:].strip()
                    confidence_value = float(confidence_str)
                    count += 1
                    total_confidence += confidence_value
    except FileNotFoundError:
        print("File not found:", file_name)

    if count > 0:
        average_confidence = total_confidence / count
        print("Average spam confidence:", average_confidence)
    else:
        print("No valid lines found in the file.")

# Application 4: Searching a File for Email Addresses
def app4():
    """
    Searches a file for lines starting with 'From ' and prints the email addresses.
    """
    fname = input("Enter file name: ")
    if len(fname) < 1:
        fname = "mbox-short.txt"

    with open(fname) as fh:
        count = 0
        for line in fh:
            if line.startswith("From "):
                email = line.split()[1]
                count += 1
                print(email)

    print("There were", count, "lines in the file with From as the first word")

# Application 5: Regular Expressions to Sum Numbers in a File
import re
def app5():
    """
    Uses regular expressions to sum all the numbers in a file specified by the user.
    """
    file_name = "regex_sum_2023969.txt"
    with open(file_name, 'r') as file:
        file_content = file.read()

    numbers = re.findall('[0-9]+', file_content)
    numbers = list(map(int, numbers))

    print('Sum of numbers:', sum(numbers))

# Application 6: Simple Socket Programming
import socket
def app6():
    """
    Connects to a website, retrieves data, and prints it to the console.
    """
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

# Application 7: Basic Web Scraping with BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
def app7():
    """
    Scrapes data from a web page and sums the values within 'span' tags.
    """
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    lost = 0
    # Retrieve all of the anchor tags
    tags = soup('span')
    for tag in tags:
        # Look at the parts of a tag
        print('Contents:', tag.contents[0])
        app = int(tag.contents[0])
        lost += app
    print(lost)

# Application 8: Advanced Web Scraping with BeautifulSoup and URL Iteration
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
def app8():
    """
    Scrapes data from a web page, retrieves data from specific anchor tags, and iterates through multiple URLs.
    """
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    count = int(input('Enter count: ')) + 1
    position = int(input('Enter position: ')) - 1

    for i in range(count):
        print('Retrieving: ' + url)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all of the anchor tags
        tags = soup('a')
        url = tags[position].get('href', None)

# The Ultimate Application: A Powerful Web Scraper and Data Analyzer
def scrape_and_analyze(url, count, position):
    """
    Scrapes data from a web page, analyzes it, and returns key insights.

    Args:
        url (str): The URL of the web page to scrape.
        count (int): The number of times to retrieve data from the URL.
        position (int): The position of the anchor tag to retrieve data from.

    Returns:
        dict: A dictionary containing key insights extracted from the data.
    """

    data = []
    for i in range(count):
        print('Retrieving: ' + url)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        url = tags[position].get('href', None)
        data.append(url)

    # Analyze the data (e.g., count occurrences, calculate statistics, etc.)
    # ...

    # Return a dictionary containing key insights
    insights = {
        'most_frequent_url': '',  # Example: Store the most frequent URL
        'average_length': 0.0,   # Example: Calculate the average URL length
        # ...
    }
    return insights

# Example usage
def app9():
    """
    Prompts the user for URL, count, and position, then runs the scrape_and_analyze function.
    """
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))

    results = scrape_and_analyze(url, count, position)
    print("Insights:", results)

# Application 10: Parsing XML Data
import urllib.request
import xml.etree.ElementTree as ET
def app10():
    """
    Retrieves XML data from a URL, parses it, and calculates the sum of 'count' values.
    """
    url = input('Enter location: ')
    if len(url) < 1 : 
        url = 'http://py4e-data.dr-chuck.net/comments_2023973.xml'

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved',len(data),'characters')
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    nums = list()
    for result in counts:
        # Debug print the data :)
        print(result.text)
        nums.append(int(result.text))

    print('Count:', len(nums))
    print('Sum:', sum(nums))

# Application 11: Parsing JSON Data
import json, urllib.request, urllib.parse, urllib.error
def app11():
    """
    Retrieves JSON data from a URL, parses it, and calculates the sum of 'count' values.
    """
    url = input('Enter location: ')
    if len(url) < 1:
        url = 'http://py4e-data.dr-chuck.net/comments_2023974.json'

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()

    print('Retrieved', len(data), 'characters')

    info = json.loads(data)
    print('User count:', len(info))
    num = list()
    for item in info['comments']:  #it's how to access inside things
        print('Name', item['name'])
        print('Count', item['count'])
        num.append(item['count'])

    print('Count', len(num))
    print('sum', sum(num))

# Application 12: Geocoding with Geoapify
import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def app12():
    """
    Retrieves geocoding data from a URL, parses it, and prints the Plus Code.
    """
    while True:
        address = input('Enter location: ')
        if len(address) < 1: break

        address = address.strip()
        parms = dict()
        parms['q'] = address

        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'features' not in js:
            print('==== Download error ===')
            print(data)
            break

        if len(js['features']) == 0:
            print('==== Object not found ====')
            print(data)
            break

        # print(json.dumps(js, indent=4))

        location = js['features'][0]['properties']['plus_code']
        print(location)

# Application 13: Extracting Numbers from Text Using Regex
import re
def app13():
    """
    Extracts numbers from text using regular expressions and calculates their sum.
    """
    text = input("Enter text: ")
    numbers = re.findall('[0-9]+', text)
    numbers = list(map(int, numbers))
    print("Sum of numbers:", sum(numbers))

# Application 14: Finding All Emails in a String
import re
def app14():
    """
    Finds all email addresses in a given string using regular expressions.
    """
    text = input("Enter text: ")
    emails = re.findall('\S+@\S+', text)
    print("Email addresses:", emails)

# Application 15: Matching Specific Patterns
import re
def app15():
    """
    Uses regular expressions to match specific patterns in text.
    """
    text = input("Enter text: ")
    pattern = input("Enter pattern: ")
    matches = re.findall(pattern, text)
    print("Matches:", matches)

# Application 16: Counting Email Organization Using SQLite
import sqlite3
def app16():
    """
    Counts the frequency of email organizations from a file using SQLite.
    """
    conn = sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Counts')

    cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)
    ''')

    fname = input('Enter file name: ')
    if (len(fname) < 1): fname = 'mbox.txt'
    fh = open(fname)
    for line in fh:
        if not line.startswith('From: '): continue
        pieces = line.split()
        email = pieces[1].split("@")
        org = email[1]

        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (org,))
        conn.commit()

    # https://www.sqlite.org/lang_select.html
    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])

    cur.close()

# Application 17: Creating a Database from a CSV File
import sqlite3
def app17():
    """
    Creates a database from a CSV file, including tables for Artist, Album, Track, and Genre.
    """
    conn = sqlite3.connect('Version6.sqlite')
    cur = conn.cursor()

    # Create fresh tables using executescript()
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
    );
    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER,
        rating INTEGER,
        count INTEGER
    );
    ''')

    # Open the CSV file
    with open('tracks.csv') as handle:
        for line in handle:
            line = line.strip()
            pieces = line.split(',')
            if len(pieces) < 7:
                continue

            name = pieces[0]
            artist = pieces[1]
            album = pieces[2]
            count = pieces[3]
            rating = pieces[4]
            length = pieces[5]
            genre = pieces[6]

            # Insert artist
            cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist,))
            cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
            artist_id = cur.fetchone()[0]

            # Insert album
            cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)''', (album, artist_id))
            cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
            album_id = cur.fetchone()[0]

            # Insert genre
            cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre,))
            cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
            genre_id = cur.fetchone()[0]

            # Insert track
            cur.execute('''INSERT OR REPLACE INTO Track
                (title, album_id, len, rating, count, genre_id)
                VALUES (?, ?, ?, ?, ?, ?)''',
                (name, album_id, length, rating, count, genre_id))

        conn.commit()

    # Close the connection
    cur.close()
    conn.close()

    # Check data with the suggested query
    conn = sqlite3.connect('Version6.sqlite')
    cur = conn.cursor()
    cur.execute('''
    SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track
    JOIN Genre ON Track.genre_id = Genre.id
    JOIN Album ON Track.album_id = Album.id
    JOIN Artist ON Album.artist_id = Artist.id
    ORDER BY Artist.name
    LIMIT 3
    ''')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    while True:
        print("Available Applications:")
        print("1. Basic Print Statements and Integer Conversion")
        print("2. Finding the Smallest Number in a List")
        print("3. Calculating Average Spam Confidence from a File")
        print("4. Searching a File for Email Addresses")
        print("5. Regular Expressions to Sum Numbers in a File")
        print("6. Simple Socket Programming")
        print("7. Basic Web Scraping with BeautifulSoup")
        print("8. Advanced Web Scraping with BeautifulSoup and URL Iteration")
        print("9. Powerful Web Scraper and Data Analyzer")
        print("10. Parsing XML Data")
        print("11. Parsing JSON Data")
        print("12. Geocoding with Geoapify")
        print("13. Extracting Numbers from Text Using Regex")
        print("14. Finding All Emails in a String")
        print("15. Matching Specific Patterns")
        print("16. Counting Email Organization Using SQLite")
        print("17. Creating a Database from a CSV File")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            app1()
        elif choice == '2':
            app2()
        elif choice == '3':
            app3()
        elif choice == '4':
            app4()
        elif choice == '5':
            app5()
        elif choice == '6':
            app6()
        elif choice == '7':
            app7()
        elif choice == '8':
            app8()
        elif choice == '9':
            app9()
        elif choice == '10':
            app10()
        elif choice == '11':
            app11()
        elif choice == '12':
            app12()
        elif choice == '13':
            app13()
        elif choice == '14':
            app14()
        elif choice == '15':
            app15()
        elif choice == '16':
            app16()
        elif choice == '17':
            app17()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")