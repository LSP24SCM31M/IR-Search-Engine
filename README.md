                                                    INFORMATION RETREIVAL
                                                   PROJECT REPORT

ABSTRACT:

The project's goal is to create a complete search engine system with an indexer, query processor, and web crawler. The main goal is to give users the ability to effectively perform free text queries to search through a corpus of web documents. The indexer, which is driven by Scikit-Learn, arranges the web information into a searchable inverted index, while the scrapy-built crawler makes it easier to obtain web content. Users can enter queries into the Flask-based processor's interface to get pertinent results.



































OVERVIEW:

In this project, we are creating a search engine that retrieves and ranks web information based on TF-IDF (Term Frequency-Inverse Document Frequency) score. The three primary parts of the suggested system and solution outline are the query processor, indexing engine, and web crawler. Several critical phases are included in the development process to guarantee accurate and powerful search capabilities. To provide the top search results based on both standard and advanced indexing techniques, two distinct APIs are established. The Scikit-Learn documentation, current semantic search research, and KNN techniques are the sources of information for this project.

DESIGN:

The system boasts a range of capabilities:

Web Crawling: Utilizing a Scrapy-based crawler, it retrieves web documents from specified URLs, observing constraints like traversal depth and maximum page count.
Indexing: Employing Scikit-Learn, it constructs an inverted index with TF-IDF scores, incorporating advanced features like word embeddings and FAISS for enhanced similarity search.
Query Processing: Through cosine similarity and TF-IDF scores, the Flask processor handles user queries, ensuring validation and returning optimal results. It also offers spell check and query expansion functionalities.

Interactions:

Web Crawling to Indexing: The indexing engine utilizes crawled web content to generate an inverted index with TF-IDF scores.
Indexing to Query Processing: The indexing engine produces an inverted index to facilitate the retrieval of relevant documents in response to user queries.
User Interaction: Users engage with the system via the Flask-based query processor, inputting queries and receiving search results.

Integration:

Two APIs facilitate search using standard and advanced indexing, interfacing with the indexing engine and query processor. Data flows from web crawling to indexing and then to the query processor. The modular design accommodates future feature additions, ensuring an efficient system for accurate search outcomes.







ARCHITECTURE:

The software architecture comprises several key components:

Web Crawler: Developed using Scrapy, this component is responsible for fetching web documents from specified URLs.
Indexing Engine: Built on Scikit-Learn, this engine performs TF-IDF indexing and offers advanced methods such as word embeddings and FAISS for enhanced indexing capabilities.
Query Processor: Implemented using Flask, this module handles user queries, conducts validation, and retrieves search results.
APIs: The system features two distinct APIs serving search results based on standard and advanced indexing methodologies.

Interfaces:

API Interfaces: Both APIs are RESTful, providing users with seamless access to search functionality.
Data Interface: Facilitating interaction between the crawler, indexing engine, and query processor, data pipelines ensure smooth data flow throughout the system.
The architecture prioritizes seamless interaction between components, fostering clear interfaces for efficient data flow. Its modular design promotes scalability and extensibility, enabling the integration of additional features and functionalities to meet evolving requirements.

OPERATION:

To commence the project operation, follow these steps to ensure seamless execution:

1.	Python and Linux Installation on Windows:
 Begin by installing Python on your Windows system.
 Next, initiate the installation of Linux on Windows Subsystem for Linux (WSL)   using the command wsl --install.
2.	Library Installation:
Install the required libraries by executing the following commands:
pip install scrapy
pip install scikit-learn
pip install beautifulsoup4
pip install flask
pip install requests
3.	Project Execution Instructions:
Step 1: Navigate to the spiders folder in your terminal and execute the command:
scrapy crawl <file_name>
This command initiates the web crawling process and computes TF-IDF scores and cosine similarity for the HTML documents, storing the results in an index.pkl file.
Step 2: Access the index.pkl file by navigating to the access pickle folder in the terminal. Run the Python file in this folder to display the contents of the file in the terminal.
Step 3: Start the Flask server by navigating to the Flask folder in the terminal and executing the Python file within that folder.
Step 4: With the Flask server now running, open a new terminal window and send a request to the server with a query in the following format:
curl -X POST http://localhost:5000/query -H "Content-Type: application/json" -d '{"query": "python"}'
Upon executing this command, you will receive a JSON-formatted response from the server, containing cosine similarity scores and document names of the top k results.
Following these steps meticulously ensures the successful operation of the project, facilitating efficient querying and retrieval of relevant information from the web documents.

CONCLUSION:

In conclusion, the project has successfully implemented both APIs, which effectively return relevant documents as output. However, there is room for improvement in the ranking of documents, as it currently requires refinement. While the Scikit-learn API demonstrates good precision in returning relevant documents for most queries, further optimization may be necessary for certain inquiries. Despite these considerations, results remain consistent across all three scenarios, showcasing the reliability of the system.

Data Sources:

The project relies on the following key libraries and tools:

Scrapy (version 2.11.1) for web crawling.
Beautiful Soup (version 4) for parsing HTML content.
Scikit-learn (version 1.4.2) for TF-IDF indexing and advanced search functionalities.
Flask (version 3.0.3) for building the query processor module.


TEST CASES:

Test cases are essential for ensuring the robustness and reliability of the system. A comprehensive test framework, harness, and coverage analysis are recommended to validate the functionality of each component thoroughly.

 
 <img width="457" alt="image" src="https://github.com/LSP24SCM31M/IR-Search-Engine/assets/164950287/1770a75c-f4ed-448a-8ee7-874f72a325dd">

 <img width="455" alt="image" src="https://github.com/LSP24SCM31M/IR-Search-Engine/assets/164950287/92544a94-2f04-422d-8aae-caa06c8ea482">

 <img width="468" alt="image" src="https://github.com/LSP24SCM31M/IR-Search-Engine/assets/164950287/c6d250b0-984d-407b-84b5-5f74f80378c3">
 



 


SOURCE CODE:

The source code is organized into distinct modules and files:

Spider file (e.g., react_beauty_spider.py) for web crawling functionality.
Scrapped pages stored in directories with names like react-{id}.
Processor logic encapsulated in processor.py, responsible for handling user queries.
Query logic implemented in query.py, facilitating query processing.
The TF-IDF index stored in a pickle file named tf-idf.pkl.
Programmatic APIs provided by manual-request.py for manual interaction.
Scikit API functionalities accessible through scikit-request.py.
The source code listings should be accompanied by comprehensive documentation, detailing dependencies and usage instructions, to facilitate ease of understanding and further development by other contributors.








BILBOGRAPHY:

https://scrapy.org/

https://requests.readthedocs.io/en/latest/

https://scikit-learn.org/stable/

https://flask.palletsprojects.com/en/3.0.x/




