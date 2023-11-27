import yaml
import os
class Flattener:
    def handleTemplate(self,v):

        print(v)
    
    def traverse(self,obj):
        match obj:
            case dict():
                for k,v in obj.items():
                    if k == "template":
                        handleTemplate(obj)
                    else:
                        traverse(v)
            case list():
                for v in obj:
                    traverse(v)
            case _:
                pass