import subprocess
import shutil
import os
import random

class RNGNull:
    def __init__(self, src_path, temp_path):
        self.src_path = src_path
        self.temp_path = temp_path

    def generate(self):
        with open(self.src_path, 'r', encoding='utf-8') as f:
            content = f.read()
        replaced = ''
        for c in content:
            if c == '\u2400':  # ␀
                replaced += str(random.randint(1, 9))
            else:
                replaced += c
        with open(self.temp_path, 'w', encoding='utf-8') as f:
            f.write(replaced)

    def cleanup(self):
        if os.path.exists(self.temp_path):
            os.remove(self.temp_path)

class LatexProjectCompiler:
    def __init__(self, project_name='RAMI_Prueba', main_tex_name='examGenerator.tex', pdf_name='examGenerator.pdf'):
        self.workspace_dir = os.getcwd()
        self.project_dir = os.path.join(self.workspace_dir, project_name)
        self.output_dir = os.path.join(self.workspace_dir, 'output')
        self.logs_dir = os.path.join(self.workspace_dir, '_logs')
        self.main_tex = os.path.join(self.project_dir, 'assets', main_tex_name)
        self.pdf_name = pdf_name
        self.pdf_path = os.path.join(self.project_dir, pdf_name)
        self.output_pdf_path = os.path.join(self.output_dir, pdf_name)
        self.aux_files = [f'{os.path.splitext(pdf_name)[0]}.{ext}' for ext in ['aux', 'log', 'out']]
        # RNGNull setup
        self.questions_src = os.path.join(self.project_dir, 'examples', 'questions.tex')
        self.questions_temp = os.path.join(self.project_dir, 'examples', 'questions_temp.tex')
        self.rngnull = RNGNull(self.questions_src, self.questions_temp)

    def ensure_directories(self):
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)

    def compile_latex(self):
        error_occurred = False
        for _ in range(2):
            try:
                subprocess.run([
                    'pdflatex',
                    '-interaction=nonstopmode',
                    '-output-directory', self.project_dir,
                    self.main_tex
                ], cwd=self.project_dir, check=True)
            except subprocess.CalledProcessError as e:
                print(f"LaTeX compilation error (exit code {e.returncode}). Attempting to move PDF if it exists...")
                error_occurred = True
                break
        return error_occurred

    def move_pdf(self, error_occurred):
        if os.path.exists(self.pdf_path):
            shutil.move(self.pdf_path, self.output_pdf_path)
            print(f"PDF generated at: {self.output_pdf_path}")
            if error_occurred:
                print("Warning: LaTeX compilation returned an error, but PDF was generated and moved.")
        else:
            print("PDF not found. Compilation may have failed.")

    def move_aux_files(self):
        for fname in self.aux_files:
            src = os.path.join(self.project_dir, fname)
            dst = os.path.join(self.logs_dir, fname)
            if os.path.exists(src):
                shutil.move(src, dst)
                print(f"Moved {fname} to _logs directory.")

    def run(self):
        self.ensure_directories()
        self.rngnull.generate()
        orig_questions = os.path.join(self.project_dir, 'examples', 'questions.tex')
        backup_questions = orig_questions + '.bak'
        shutil.copy2(orig_questions, backup_questions)
        shutil.copy2(self.questions_temp, orig_questions)
        try:
            error_occurred = self.compile_latex()
            self.move_pdf(error_occurred)
            self.move_aux_files()
        finally:
            shutil.move(backup_questions, orig_questions)
            self.rngnull.cleanup()

if __name__ == "__main__":
    compiler = LatexProjectCompiler()
    compiler.run()