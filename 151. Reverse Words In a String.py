import re
class Solution(object):
    def reverseWords(self, s):

        word_list = []
        word_list = re.split(' +',s)

        new_string = ""

        while(len(word_list) > 0):
            new_word = word_list.pop(len(word_list) - 1)            
            new_word = " " + new_word
            new_string += new_word
        
        new_string = new_string.strip()
        return new_string