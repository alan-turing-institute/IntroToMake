# Intro to Make
Author: [G.J.J. van den Burg](https://gertjan.dev)

Below is the Makefile I used to create this repo.

```Makefile

# A makefile for the repo! How meta!
#

.POSIX:

REPO_DIR = ./actual_repo
SOURCE_DIR = ./sources
BIG_DATA_CSV = $(wildcard $(SOURCE_DIR)/big_data/*.csv)
REPO_URL = https://github.com/alan-turing-institute/IntroToMake

.PHONY: all clean repo push init makefiles

all: repo magic push

repo: init makefiles

init: init_dir init_data init_report init_script init_output_dir init_remote init_readme init_license

makefiles: make_call


########
# INIT #
########

init_dir:
	mkdir $(REPO_DIR)
	mkdir $(REPO_DIR)/{data,report,scripts,output}
	cd $(REPO_DIR) && git init .

init_data: init_dir $(SOURCE_DIR)/input_file_1.csv $(SOURCE_DIR)/input_file_2.csv
	cp $(SOURCE_DIR)/input_file_{1,2}.csv $(REPO_DIR)/data
	cd $(REPO_DIR) && git add data/input_file_{1,2}.csv
	cd $(REPO_DIR) && git commit -am "add datasets" && sleep 1

init_report: init_dir $(SOURCE_DIR)/report.tex
	cp $(SOURCE_DIR)/report.tex $(REPO_DIR)/report
	cd $(REPO_DIR) && git add report/report.tex && git commit -am "add report" && sleep 1
	echo -e "*.aux\n*.log" > $(REPO_DIR)/report/.gitignore
	cd $(REPO_DIR) && git add report/.gitignore && git commit -am "add report gitignore" && sleep 1

init_script: init_dir $(SOURCE_DIR)/generate_histogram.py
	cp $(SOURCE_DIR)/generate_histogram.py $(REPO_DIR)/scripts
	cd $(REPO_DIR) && git add scripts/generate_histogram.py && \
		git commit -am "add histogram script" && sleep 1

init_output_dir: init_dir
	echo -e "*\n!.gitignore" > $(REPO_DIR)/output/.gitignore
	cd $(REPO_DIR) && git add output/.gitignore && git commit -am "add output dir" && sleep 1

init_remote: init_dir
	cd $(REPO_DIR) && git remote add origin $(REPO_URL)

init_readme: init_dir $(SOURCE_DIR)/README.md
	cp $(SOURCE_DIR)/README.md $(REPO_DIR)/README.md
	cd $(REPO_DIR) && git add README.md
	cd $(REPO_DIR) && git commit -am "add readme" && sleep 1

init_license: init_dir $(SOURCE_DIR)/LICENSE
	cp $(SOURCE_DIR)/LICENSE $(REPO_DIR)/LICENSE
	cd $(REPO_DIR) && git add LICENSE
	cd $(REPO_DIR) && git commit -am "add license" && sleep 1

############
# BRANCHES #
############

big_data: $(BIG_DATA_CSV) $(SOURCE_DIR)/report_big_data.tex
	cd $(REPO_DIR) && git checkout master && git branch big_data && git checkout big_data
	cp $(BIG_DATA_CSV) $(REPO_DIR)/data
	cd $(REPO_DIR) && git add data/*.csv && \
		git commit -am "add more datasets" && sleep 1
	cp $(SOURCE_DIR)/report_big_data.tex $(REPO_DIR)/report/report.tex
	cd $(REPO_DIR) && git add ./report/report.tex && git commit -am "update report for big data" && sleep 1

#############
# MAKEFILES #
#############

make_basics: $(SOURCE_DIR)/Makefile_basics init
	cd $(REPO_DIR) && git branch follow_along && git checkout follow_along
	cp $< $(REPO_DIR)/Makefile
	cd $(REPO_DIR) && git add Makefile && git commit -am "Makefile no. 1 (The Basics)" && sleep 1

make_all_clean: $(SOURCE_DIR)/Makefile_all_clean make_basics
	cd $(REPO_DIR) && git checkout follow_along
	cp $< $(REPO_DIR)/Makefile
	cd $(REPO_DIR) && git add Makefile && git commit -am "Makefile no. 2 (all and clean)" && sleep 1

make_phony: $(SOURCE_DIR)/Makefile_phony make_all_clean
	cd $(REPO_DIR) && git checkout follow_along
	cp $< $(REPO_DIR)/Makefile
	cd $(REPO_DIR) && git add Makefile && git commit -am "Makefile no. 3 (Phony Targets)" && sleep 1

make_var_and_pat: $(SOURCE_DIR)/Makefile_var_and_pat make_phony
	cd $(REPO_DIR) && git checkout follow_along
	cp $< $(REPO_DIR)/Makefile
	cd $(REPO_DIR) && git add Makefile && \
		git commit -am "Makefile no. 4 (Automatic Variables and Pattern Rules)" && sleep 1

make_wildcard: $(SOURCE_DIR)/Makefile_wildcard make_var_and_pat | big_data
	cd $(REPO_DIR) && git checkout follow_along && git merge --no-edit big_data
	cp $< $(REPO_DIR)/Makefile
	cd $(REPO_DIR) && git add Makefile && \
		git commit -am "Makefile no. 5 (Wildcards and Path Substitution)" && sleep 1

make_with_qq: $(SOURCE_DIR)/Makefile_with_qq make_wildcard
	cd $(REPO_DIR) && git checkout follow_along
	cd $(REPO_DIR) && git branch canned && git checkout canned
	cp $< $(REPO_DIR)/Makefile
	cp $(SOURCE_DIR)/report_with_qq.tex $(REPO_DIR)/report/report.tex
	cp $(SOURCE_DIR)/generate_qqplot.py $(REPO_DIR)/scripts/generate_qqplot.py
	cd $(REPO_DIR) && git add Makefile report/report.tex scripts/generate_qqplot.py && \
		git commit -am "Makefile (intermediate, with QQ-plot changes)" && sleep 1

make_call: $(SOURCE_DIR)/Makefile_call make_with_qq
	cd $(REPO_DIR) && git checkout follow_along && git merge --no-edit canned
	cp $< $(REPO_DIR)/Makefile
	cd $(REPO_DIR) && git add Makefile && \
		git commit -am "Makefile no. 6 (Advanced: Generating Rules using Call)" && sleep 1

#########
# OTHER #
#########

magic: repo
	cd $(REPO_DIR) && git branch magic && git checkout magic
	echo -e "# Intro to Make\nAuthor: [G.J.J. van den Burg](https://gertjan.dev)\n" > $(REPO_DIR)/MAGIC.md
	echo -e "Below is the Makefile I used to create this repo.\n\n\`\`\`Makefile\n" >> $(REPO_DIR)/MAGIC.md
	cat ./Makefile >> $(REPO_DIR)/MAGIC.md
	echo -e "\`\`\`\n" >> $(REPO_DIR)/MAGIC.md
	cd $(REPO_DIR) && git add MAGIC.md && git commit -am "add some magic" && sleep 1

push: repo magic
	cd $(REPO_DIR) && git push -f -u --all origin

clean:
	rm -rf $(REPO_DIR)
```

