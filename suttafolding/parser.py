import re
import json


class MatikaParser():
    def __init__(self):
        self.matikas = {}
        self.current_entry = None
        self.section_re = re.compile("^## *(.*)$")
        self.list_re = re.compile("^\* *(.*)$")
        self.idline_re = re.compile("^id\: +([a-zA-Z0-9.\-\_ ]+)$")
        self.pali_re = re.compile("\(@\[p\]([a-zA-Z0-9\.\-\_ ]+)\)")


    def parse_file(self, filepath):
        with open(filepath, 'r') as ifile:
            self.parse_content(ifile.read())

    def parse_content(self, content):
        self.open_content()
        for line in content.split('\n'):
            self.parse_line(line)
        self.close_content()

    def open_content(self):
        self.matikas = {}
        self.current_entry = None

    def close_content(self):
        if self.current_entry != None:
            self.close_section()

    def parse_line(self, line):
        sectionlabel = self.section_re.match(line)
        if sectionlabel:
            self.open_section(sectionlabel.group(1))
            return

        listlabel = self.list_re.match(line)
        if listlabel:
            self.list_element(listlabel.group(1))
            return

        keyline = self.idline_re.match(line)
        if keyline:
            self.id_element(keyline.group(1))
            return

    def open_section(self, group):
        # beginning with ##
        label = group
        if self.current_entry != None:
            self.close_section()
        self.current_entry = {}
        #self.current_entry['key'] = label
        self.current_entry['elements'] = []

    def id_element(self, group):
        self.current_entry['key'] = group

    def list_element(self, group):
        pali = self.pali_re.findall(group)
        if len(pali)>0:
            self.current_entry['elements'].append(" ".join(pali))
        else:
            self.current_entry['elements'].append(group)

    def close_section(self):
        if self.current_entry == None:
            return
        if 'key' in self.current_entry:
            self.matikas[self.current_entry['key']] = self.current_entry
        self.current_entry = None


if __name__ == '__main__':
    parser = MatikaParser()

    parser.parse_file('../data/matikas.md')
    print(json.dumps(parser.matikas, indent=1))
