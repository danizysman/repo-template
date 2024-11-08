# true-neutral-cookiecutter
A minimalist cookiecutter for research and data science projects
pip install cookiecutter
Run via `cookiecutter gh:danizysman/repo-template`
cd {{cookiecutter.repo_name}}
conda create --name {{cookiecutter.repo_name}} python=3.11
conda activate {{cookiecutter.repo_name}}
conda env export --name machine-learning-env --from-history --file environment.yml
pip install pipreqs
pipreqs to generate requirements.txt

