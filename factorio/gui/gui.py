#!/usr/bin/env python3
"""Factorio utils"""

import json
import tkinter as tk
from tkinter import ttk

from factorio.bp import blueprint_to_constant_combinator, decode, encode

# pylint: disable=broad-exception-caught


class App:
    """Application class."""

    INDENT: int = 1

    bp_text: tk.Text
    status_bar: ttk.Label
    search_btn = ttk.Button

    def __init__(self):
        self.root = tk.Tk()
        self.search_term = tk.StringVar()
        self.positions = []
        self.current_idx = -1
        self._init_gui()

    def _init_gui(self) -> None:
        """Initialize the GUI."""
        self.root.title("Factorio Utilities")
        main_fr = ttk.Frame(self.root)
        main_fr.grid(sticky="nwes")

        self._init_action_frame(main_fr)
        self._init_blueprint_text(main_fr)
        self._init_status_bar(main_fr)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_fr.columnconfigure(0, weight=1)
        main_fr.rowconfigure(1, weight=1)

    def _init_action_frame(self, root: ttk.Frame) -> None:
        """Initialize the labeled frame with buttons."""
        label_fr = ttk.LabelFrame(root, text="Actions")
        label_fr.grid(padx=5, pady=3, ipady=3, sticky="nwe")
        ttk.Button(label_fr, text="Paste as BP", command=self.on_paste_btn).grid(row=0, column=0, pady=3, sticky="w")
        ttk.Button(label_fr, text="Create CC", command=self.on_create_cc_btn).grid(row=0, column=1, pady=3, sticky="w")
        ttk.Button(label_fr, text="Copy as B64", command=self.on_copy_btn).grid(row=0, column=2, pady=3, sticky="w")
        search = ttk.Entry(label_fr, textvariable=self.search_term, width=25)
        search.grid(row=0, column=4, pady=3, sticky="e")
        search.bind("<Return>", self.on_search_btn)
        ttk.Button(label_fr, text="Search", command=self.on_search_btn).grid(row=0, column=5, pady=3, sticky="e")
        self.search_btn = ttk.Button(label_fr, text="Next", command=self.on_next_btn, state=tk.DISABLED)
        self.search_btn.grid(row=0, column=6, pady=3, sticky="e")
        label_fr.columnconfigure(3, weight=1)

    def _init_blueprint_text(self, root: ttk.Frame) -> None:
        """Initialize the blueprint (text) area."""
        label_fr = ttk.LabelFrame(root, text="Blueprint")
        label_fr.grid(padx=5, pady=3, ipady=3, sticky="nwes")
        self.bp_text = tk.Text(label_fr, width=80, height=25, state=tk.NORMAL, wrap="none")
        ys = ttk.Scrollbar(label_fr, orient="vertical", command=self.bp_text.yview)
        xs = ttk.Scrollbar(label_fr, orient="horizontal", command=self.bp_text.xview)
        self.bp_text["yscrollcommand"] = ys.set
        self.bp_text["xscrollcommand"] = xs.set
        self.bp_text.grid(column=0, row=0, padx=5, pady=3, sticky="nwes")
        xs.grid(column=0, row=1, sticky="we")
        ys.grid(column=1, row=0, sticky="ns")
        label_fr.rowconfigure(0, weight=1)
        label_fr.columnconfigure(0, weight=1)

    def _init_status_bar(self, root: ttk.Frame) -> None:
        """Initialize the status bar"""
        status_fr = ttk.Frame(root, relief=tk.SUNKEN)
        status_fr.grid(padx=5, pady=3, sticky="ws")
        self.status_bar = ttk.Label(status_fr, text="Ready...")
        self.status_bar.grid(sticky="w")

    def _reset_search(self) -> None:
        self.bp_text.tag_remove("found", "1.0", tk.END)
        self.positions = []
        self.current_idx = -1
        self.search_btn.configure(state=tk.DISABLED)  # type: ignore

    def _update_status_bar(self, message: str) -> None:
        """Update the status bar with a new message."""
        self.status_bar.config(text=message)

    def _update_blueprint_text(self, blueprint_text: str, message: str) -> None:
        """Update the blueprint text area."""
        self.bp_text.delete(1.0, tk.END)
        self.bp_text.insert(1.0, blueprint_text)
        self._reset_search()
        self.search_term.set("")
        self._update_status_bar(message)

    def on_paste_btn(self) -> None:
        """Handle [Paste] button."""
        try:
            clipboard_content = self.root.clipboard_get()
        except tk.TclError:
            return
        try:
            if "{" in clipboard_content:
                # JSON structure -> blueprint
                blueprint = json.loads(clipboard_content)
            else:
                # BASE64 -> encoded blueprint
                blueprint = decode(clipboard_content)
            blueprint_text = json.dumps(blueprint, indent=self.INDENT)
        except Exception:
            # ignore errors: just paste whatever we got as text
            blueprint_text = str(clipboard_content)
        self._update_blueprint_text(blueprint_text, "Clipboard pasted...")

    def on_copy_btn(self) -> None:
        """Handle [Copy] button"""
        try:
            blueprint = json.loads(self.bp_text.get(1.0, tk.END))
            blueprint_b64 = encode(blueprint)
        except Exception:
            self._update_status_bar("ERROR: could not encode blueprint...")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(blueprint_b64)
        self._update_status_bar("Blueprint copied to clipboard...")

    def on_create_cc_btn(self) -> None:
        """Handle [Create CC] button click."""
        try:
            blueprint = json.loads(self.bp_text.get(1.0, tk.END))
            cc_blueprint = blueprint_to_constant_combinator(blueprint)
            blueprint_text = json.dumps(cc_blueprint, indent=self.INDENT)
        except Exception:
            self._update_status_bar("ERROR: could not create Constant Combinator blueprint...")
            return
        self._update_blueprint_text(blueprint_text, "Constant combinator created...")

    def on_search_btn(self, _: tk.Event | None = None) -> None:
        """Handle [Search] button click."""
        self._reset_search()
        if not (search_term := self.search_term.get()):
            return

        start_pos = "1.0"
        while True:
            idx = self.bp_text.search(search_term, start_pos, stopindex=tk.END)
            if not idx:
                break
            end_pos = f"{idx}+{len(search_term)}c"
            self.bp_text.tag_add("found", idx, end_pos)
            self.positions.append((idx, end_pos))
            start_pos = end_pos
        self.bp_text.tag_config("found", foreground="red", background="yellow")
        if not self.positions:
            self._update_status_bar("Not found...")
        else:
            self.search_btn.configure(state=tk.NORMAL)  # type: ignore
            self.on_next_btn()

    def on_next_btn(self) -> None:
        """Handle [Next] button click."""
        if not self.positions:
            return
        self.current_idx = (self.current_idx + 1) % len(self.positions)
        self._update_status_bar(f"Entry: {self.current_idx + 1}/{len(self.positions)}")
        start_pos = self.positions[self.current_idx][0]
        self.bp_text.mark_set("insert", start_pos)
        self.bp_text.see(start_pos)
        self.bp_text.focus()

    def run(self) -> None:
        """Run the main loop."""
        self.root.mainloop()


def main() -> None:
    """Main function."""
    App().run()


if __name__ == "__main__":
    main()
