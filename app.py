from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Sample dataset data
datasets = [
    {"id": 1, "title": "here we go", "description": "baba black sheep", "author": "Mr papu", "date": "2024-03-15"},
        {"id": 2, "title": "rhyme2", "description": "wheel on the bus go round and round", "author": "smurf cat", "date": "2024-03-10"},
            {"id": 3, "title": "rhyme3", "description": "baby shark doo doo", "author": "snitcher of the decade", "date": "2024-03-05"},
            ]

            # Home route
            @app.route('/')
            @app.route('/datasets')
            def datasets_page():
                search_query = request.args.get('search', '').lower()
                    filtered_datasets = [d for d in datasets if search_query in d["title"].lower() or search_query in d["description"].lower()]
                        return render_template('datasets.html', datasets=filtered_datasets, search_query=search_query)

                        # Upload route
                        @app.route('/upload', methods=['GET', 'POST'])
                        def upload_page():
                            if request.method == 'POST':
                                    title = request.form['title']
                                            description = request.form['description']
                                           date = datetime.datetime.now().strftime("%Y-%m-%d")                                                  new_dataset = {"id": len(datasets) + 1, "title": title, "description": description, "author": "Anonymous", "date": date}
                                                                    datasets.append(new_dataset)
                                                                            return redirect(url_for('datasets_page'))
                                                                                return render_template('upload.html')

                                                                                # Run the application
                                                                                if __name__ == '__main__':
                                                                                    app.run(debug=True)Flask