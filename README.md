# Markdown Converter +  

A simple app that uses pandoc to convert markdown files to HTML and places it in a unified folder (HTMLs) so that it automatically has a customized style upon conversion.  

## Usage  
To use, simply clone the git repo and use the following command:  
```sh
python3 script.py your_markdown_file.md
```

For example, if you have a markdown file called `myDotFiles.md` saved in the Markdowns folder, run the following command:
```sh
python3 script.py Markdowns/myDotFiles.md
```

## Adding bash shortcut
If you are on linux, you can create a shortcut keyword to make it work anywhere. Simply follow these steps:  
1. Open the cloned folder in terminal
2. Type `pwd` to get the full path of the folder
3. Append `script.py` to the result you got from running `pwd` to get the full path of the script. Let us call this `script_path`.
4. open `.bashrc` (in your home directory stored as a hidden file)
5. Add the following line, replacing:  
   - `emd` with your prefered shortcut command
   - `script_path` with the result you got from steps 1-3  

```
alias emd='python3 script_path'
```

So that next time you encounter a markdown file (for example, `Mark_Zuckerdown.md`) anywhere, you can just run terminal in that folder and run `emd Mark_Zuckerdown.md`, and it will automatically generate and place the HTML in the HTMLs folder (with the customized theme).  

## Dependencies  

- **lxml:**
  ```
  pip install lxml
  ```

- **pandoc:** install instructions [`here`](https://pandoc.org/installing.html)