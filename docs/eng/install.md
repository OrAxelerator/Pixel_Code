# Installation - avanced


### Installation on:
<details>
<summary><strong>1. Ubuntu/Linux</strong></summary>

* If **pipx isn't installed:**
    
    ```bash
    sudo apt install pipx
    pipx ensurepath
    ```
* Clone the repo and install the TUI:

    ```bash
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Downloads/Pixel_Code
    pipx install .
    ```
</details>

---
<details>
<summary><strong>2. MacOS</strong></summary>


* Clone the repo and install the TUI:

    ```cmd
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pip install -e .
    ```
    
</details>

---

<details>
<summary><strong>3. Windows</strong></summary>


* Download the project and install the tool:
    ```cmd
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd ./Downloads/Pixel_Code
    py -m pip install -e .
    ```
    Normally with v0.4.0 the only error you can get is :
    - pip ins't install
    - you do python but you're computer use py 
    
* Or if you get this issus : 
    ```
    WARNING: The script xxx.exe is installed in 'C:\Users\XXX\AppData\Local\Microsoft\WindowsApps' which is not on PATH
    ```
    You surely use python from MicrosoftStore (bad)
    Go download python on the official website : [python.org](https://www.python.org/)

    Download pip with python : 
    * py -m ensurepip --upgrade
    * py -m pip install --upgrade pip
    * If you get an error:
        
        
        <details>
        <summary>other error :</summary>
    
            2. Win + R 
            3. in the popup write : sysdm.cpl
            4. avanced tab
            5. variables d'environement
            6. User variable → select Path
            7. Edit
            8. New
            9. Paste this path here (change with your username) : C:\Users\**USERNAME**\AppData\Local\Python\pythoncore-3.14-64\Scripts
            10. OK -> OK -> OK
            11. Quit and re-open cmd after that.
        
            issu solved (normally)
        </details>


</details>

--- 
and execute fisrt_use.py 