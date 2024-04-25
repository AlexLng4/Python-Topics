#the arguments captured by * content are as tuple 
#keyword arguments not explicitly named in the tag signature are captured by
#**attrs as a dict.
#The cls parameter can only be passed as a keyword argument.

def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />'%(name, attr_str)
    
tag('name',"hello", "world", "alex",id=33,p=23,l=34)

#optain information about the args function
# also can use oder varibles
import inspect
sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset',
          'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)

tag.__code__
tag.__defaults__ # default values for args
tag.__code__.co_varnames # name of the args
tag.__code__.co_argcount # numeber of args

print("Stop")
    