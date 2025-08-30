"""
Projeto: Organizador de Arquivos
Autor: Márcio Ferreira
Descrição:
    Aplicação simples em Python para organizar arquivos em pastas
    baseadas em suas extensões. Desenvolvido com CustomTkinter para
    fornecer uma interface gráfica moderna e fácil de usar.
"""

import shutil
from pathlib import Path
from typing import Union

import customtkinter as ctk
from tkinter import filedialog, messagebox


# Configurações de aparência
APPEARANCE_MODE = "dark"      # opções: "light", "dark", "system"
COLOR_THEME = "blue"          # opções: "blue", "green", "dark-blue"
WINDOW_TITLE = "Organizador de Arquivos"
WINDOW_SIZE = "400x200"


def organizar_arquivos(pasta: Union[str, Path]) -> int:
    """
    Organiza arquivos em subpastas de acordo com sua extensão.

    Args:
        pasta: Caminho da pasta a ser organizada.

    Returns:
        int: Quantidade de arquivos movidos.
    """
    pasta = Path(pasta)

    if not pasta.exists():
        messagebox.showerror("Erro", f"A pasta '{pasta}' não existe.")
        return 0

    arquivos_movidos = 0

    for arquivo in pasta.iterdir():
        if not arquivo.is_file():
            continue

        # Define a extensão ou usa "OUTROS"
        extensao = arquivo.suffix[1:].upper() if arquivo.suffix else "OUTROS"

        destino = pasta / extensao
        destino.mkdir(exist_ok=True)

        novo_caminho = destino / arquivo.name

        # Garante nomes únicos para não sobrescrever arquivos
        contador = 1
        while novo_caminho.exists():
            novo_caminho = destino / f"{arquivo.stem}_{contador}{arquivo.suffix}"
            contador += 1

        shutil.move(str(arquivo), str(novo_caminho))
        arquivos_movidos += 1

    return arquivos_movidos


class OrganizadorApp(ctk.CTk):
    """Aplicação principal da interface gráfica."""

    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_SIZE)
        self.resizable(False, False)

        self._construir_interface()

    def _construir_interface(self) -> None:
        """Monta os elementos da interface gráfica."""
        titulo = ctk.CTkLabel(
            self,
            text="Organizador de Arquivos",
            font=("Arial", 20, "bold"),
        )
        titulo.pack(pady=10)

        frame = ctk.CTkFrame(self)
        frame.pack(pady=10, padx=20, fill="x")

        self.entrada_pasta = ctk.CTkEntry(
            frame,
            placeholder_text="Selecione a pasta...",
            width=250,
        )
        self.entrada_pasta.pack(side="left", padx=5, pady=10)

        btn_browse = ctk.CTkButton(
            frame,
            text="Procurar",
            command=self._selecionar_pasta,
        )
        btn_browse.pack(side="left", padx=5)

        btn_executar = ctk.CTkButton(
            self,
            text="Organizar",
            command=self._executar_organizacao,
            width=150,
        )
        btn_executar.pack(pady=15)

    def _selecionar_pasta(self) -> None:
        """Abre o seletor de pastas e preenche o campo de entrada."""
        pasta = filedialog.askdirectory()
        if pasta:
            self.entrada_pasta.delete(0, ctk.END)
            self.entrada_pasta.insert(0, pasta)

    def _executar_organizacao(self) -> None:
        """Executa a organização de arquivos e exibe o resultado."""
        pasta = self.entrada_pasta.get().strip()
        if not pasta:
            messagebox.showwarning("Atenção", "Por favor, selecione uma pasta.")
            return

        total = organizar_arquivos(pasta)
        messagebox.showinfo("Concluído", f"Organização finalizada! {total} arquivos movidos.")


def main() -> None:
    """Função principal para iniciar a aplicação."""
    ctk.set_appearance_mode(APPEARANCE_MODE)
    ctk.set_default_color_theme(COLOR_THEME)

    app = OrganizadorApp()
    app.mainloop()


if __name__ == "__main__":
    main()

