Dashboard created to speed up product edscribing process. It uses BS4 for webscraping content from Amazon pl/de/fr and based on it user can give promt to ChatGPT to build summary of description.

Main page - to start scraping process click on "start scraping" button and if you want program to download images from description select check boc.
<a href="https://drive.google.com/uc?export=view&id=1rUr2dLjTwhEfaacnBz8xBVMhudxrqCTG"><img src="https://drive.google.com/uc?export=view&id=1rUr2dLjTwhEfaacnBz8xBVMhudxrqCTG" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

App uses threading to speed up proces so, after about 5 - 10 sec descriptions will apear on the screen.
<a href="https://drive.google.com/uc?export=view&id=1iVcUjHzDeUmrwqE8QWbDCtUN5WbLWHEi"><img src="https://drive.google.com/uc?export=view&id=1iVcUjHzDeUmrwqE8QWbDCtUN5WbLWHEi" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

To use chat gpt first you have to provide OpenAI acces key in source code(dashboard.py - line 45) and then you can interact with ChatGpt 3.5 by pasting relevant infromation from Amazon description as showed bellow. 
<a href="https://drive.google.com/uc?export=view&id=1J0nAIR8ccMDX4pnLvI43rXEyGXhGoAHd"><img src="https://drive.google.com/uc?export=view&id=1J0nAIR8ccMDX4pnLvI43rXEyGXhGoAHd" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

Images are saved in "images" folder and each of products pictures are saved in folder wich name corresponds to ASIN code.
<a href="https://drive.google.com/uc?export=view&id=1mZddai_VX93xLSkbkI0AvGlLQfnI6hp9"><img src="https://drive.google.com/uc?export=view&id=1mZddai_VX93xLSkbkI0AvGlLQfnI6hp9" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

