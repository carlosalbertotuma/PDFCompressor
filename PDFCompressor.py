import subprocess
import sys

def banner():
    texto = r"""
                                            ########  ########  ########                                                  
                      ##   ##   ##   ##     ##     ## ##     ## ##           ##   ##   ##   ##                            
                       ## ##     ## ##      ##     ## ##     ## ##            ## ##     ## ##                             
                     ######### #########    ########  ##     ## ######      ######### #########                           
                       ## ##     ## ##      ##        ##     ## ##            ## ##     ## ##                             
                      ##   ##   ##   ##     ##        ##     ## ##           ##   ##   ##   ##                            
                                            ##        ########  ##                               By Bl4dsc4n - V.01

  ## ##       ######   #######  ##     ## ########  ########  ########  ######   ######   #######  ########       ## ##   
  ## ##      ##    ## ##     ## ###   ### ##     ## ##     ## ##       ##    ## ##    ## ##     ## ##     ##      ## ##   
#########    ##       ##     ## #### #### ##     ## ##     ## ##       ##       ##       ##     ## ##     ##    ######### 
  ## ##      ##       ##     ## ## ### ## ########  ########  ######    ######   ######  ##     ## ########       ## ##   
#########    ##       ##     ## ##     ## ##        ##   ##   ##             ##       ## ##     ## ##   ##      ######### 
  ## ##      ##    ## ##     ## ##     ## ##        ##    ##  ##       ##    ## ##    ## ##     ## ##    ##       ## ##   
  ## ##       ######   #######  ##     ## ##        ##     ## ########  ######   ######   #######  ##     ##      ## ##   
"""
    print(texto)

def comprimir_pdf(entrada, saida):
    try:
        comando = [
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS=/printer",  # /screen /ebook /printer /prepress
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={saida}",
            entrada
        ]
        subprocess.run(comando, check=True)
        print(f"[+] PDF comprimido com sucesso: {saida}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    banner()
    if len(sys.argv) != 3:
        print("Uso: python3 PDFCompressor.py entrada.pdf saida.pdf")
    else:
        comprimir_pdf(sys.argv[1], sys.argv[2])
