#!/usr/bin/env bash
# Variable
PROJECT := arpy
COMMAND := arpy
COMMAND_JW := بايثون

REMOVE_CMD := rm
MAKEDIR_CMD := mkdir
COPY_CMD := cp
RECURSIVE_FLAG := -r
RECURSIVE_FINAL_FLAG :=  -rf

.PHONY : install clean make_dir copy_dir move_cmd print_status

install: clean make_dir copy_dir move_cmd print_status

make_dir:
	@mkdir ${HOME}/${PROJECT}
	@mkdir ${HOME}/${PROJECT}/bin
	@mkdir ${HOME}/${PROJECT}/arpy

copy_dir:
	@cp -r bin/* ${HOME}/${PROJECT}/bin
	@cp -r arpy/* ${HOME}/${PROJECT}/arpy
	@cp start.py ${HOME}/${PROJECT}

# Adding class path
#export PATH=${HOME}/${PROJECT}/bin:$PATH

move_cmd:
	@mv ${HOME}/${PROJECT}/bin/cmd.sh ${HOME}/${PROJECT}/bin/${COMMAND}
	@chmod +x  ${HOME}/${PROJECT}/bin/${COMMAND}
#	@ln ${HOME}/${PROJECT}/bin/${COMMAND} ${HOME}/${PROJECT}/bin/ي
	@ln -s ${HOME}/${PROJECT}/bin/${COMMAND} /usr/local/bin/${COMMAND}
	@ln -s ${HOME}/${PROJECT}/bin/${COMMAND} /usr/local/bin/${COMMAND_JW}

print_status:
	@echo "Installation successful"
	@echo "تم التثبيت بنجاح"
#	@echo "Next Add 'export PATH=${HOME}/${PROJECT}/bin:\$$PATH' to your .bash_profile or .bashrc"
#	@echo " '.bash_profile ꦲꦸꦠꦮ .bashrc ꦤꦁ 'export PATH=${HOME}/${PROJECT}/bin:\$$PATH' ꦱꦧꦚ꧀ꦗꦸꦂꦫꦺꦤꦩ꧀ꦧꦃꦏꦺ"

clean:
	@rm -rf ${HOME}/${PROJECT}
	@rm -f /usr/local/bin/${COMMAND}
	@rm -f /usr/local/bin/${COMMAND_JW}