#!/usr/bin/env python
import os, sys

from django.core.management import execute_from_command_line as django_execute
import django_db_only


def show_usage():
	print("Usage: " + os.path.basename(sys.argv[0]) + " startproject [projectname]")
	return

def execute_from_command_line():

	if len(sys.argv) < 3:
		show_usage()
		sys.exit(1)

	cmd = sys.argv[1]
	if cmd.lower()!="startproject":
		show_usage()
		sys.exit(1)

	projectname = sys.argv[2]

	sys.argv.append("--template")
	templ_path = os.path.join(os.path.dirname(django_db_only.__file__), "conf/project_template")
	sys.argv.append(templ_path)

	django_execute(sys.argv)

	return

