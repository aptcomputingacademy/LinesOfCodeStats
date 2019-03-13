Last login: Mon Mar 11 21:03:38 on ttys005
Kamals-MacBook-Air:Projects kamalmukiri$ pwd
/Users/kamalmukiri/Documents/AptComputingAcademy/Python/Projects
Kamals-MacBook-Air:Projects kamalmukiri$ mkdir web_scrapping
Kamals-MacBook-Air:Projects kamalmukiri$ cd web_scrapping/
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ vim get_scricket_score.py
Kamals-MacBook-Air:web_scrapping kamalmukiri$ ls
get_scricket_score.py
Kamals-MacBook-Air:web_scrapping kamalmukiri$ ls
get_scricket_score.py
Kamals-MacBook-Air:web_scrapping kamalmukiri$ ls
get_scricket_score.py
Kamals-MacBook-Air:web_scrapping kamalmukiri$ vim get_scricket_score.py
Kamals-MacBook-Air:web_scrapping kamalmukiri$ python3 get_scricket_score.py 
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/client.py", line 1016, in _send_output
    self.send(msg)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/client.py", line 956, in send
    self.connect()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/client.py", line 1392, in connect
    server_hostname=server_hostname)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ssl.py", line 412, in wrap_socket
    session=session
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ssl.py", line 853, in _create
    self.do_handshake()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ssl.py", line 1117, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "get_scricket_score.py", line 7, in <module>
    html = urlopen(url)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 525, in open
    response = self._open(req, data)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 543, in _open
    '_open', req)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 503, in _call_chain
    result = func(*args)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)>
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ ssh kamal@192.168.1.102
^C
Kamals-MacBook-Air:web_scrapping kamalmukiri$ ssh kamal@192.168.1.101
The authenticity of host '192.168.1.101 (192.168.1.101)' can't be established.
ECDSA key fingerprint is SHA256:UfIpQ2wbJP1Rsb3QnduKGZMf9hwuiILmmPbWkKJkBzQ.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.1.101' (ECDSA) to the list of known hosts.
kamal@192.168.1.101's password: 
Welcome to Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-29-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

458 packages can be updated.
198 updates are security updates.

Last login: Sat Mar  9 06:43:06 2019 from 192.168.43.35
kamal@kamal-VirtualBox:~$ 
kamal@kamal-VirtualBox:~$ 
kamal@kamal-VirtualBox:~$ cd AptComputingAcademy/Cpp/
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ mkdir strings
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ vim input.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ c++ input.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ ./a.out 
kamal
Name = kamal
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ ./a.out 
kamal kumar
Name = kamal
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ c++ input.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ vim input.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ c++ input.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ ./a.out 
kamal kumar mukiri
Name = kamal kumar mukiri
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ mdkir filehandling
cd 
Command 'mdkir' not found, did you mean:

  command 'mkdir' from deb coreutils
  command 'mdir' from deb mtools

Try: sudo apt install <deb name>

kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ mkdir filehandling
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ cd filehandling/
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ c++ sample.cpp
sample.cpp: In function 'int main()':
sample.cpp:11:8: error: 'readline' was not declared in this scope
  while(readline(file, line))
        ^~~~~~~~
sample.cpp:11:8: note: suggested alternative: 'getline'
  while(readline(file, line))
        ^~~~~~~~
        getline
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ c++ sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ ./a.out 
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream file;
	file.open("sample.cpp");

	string line;
	while(getline(file, line))
	{
		cout << line << endl;
	}
	file.close();
}
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/filehandling$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ c++ new_del.cpp
new_del.cpp: In function 'int main()':
new_del.cpp:19:17: error: base operand of '->' has non-pointer type 'stud'
     cout << S[1]->data << endl;
                 ^~
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ vim new_del.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ c++ new_del.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ ./a.out 
Constructor Used
0
Destructor Used
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ vim new_del.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ c++ new_del.cpp
new_del.cpp: In function 'int main()':
new_del.cpp:18:17: error: initializer fails to determine size of 'S'
     stud* S[] = new stud[10];
                 ^~~~~~~~~~~~
new_del.cpp:18:17: error: array must be initialized with a brace-enclosed initializer
new_del.cpp:20:14: warning: deleting array 'S'
     delete[] S;
              ^
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ vim new_del.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ c++ new_del.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ ./a.out 
Constructor Used
Constructor Used
Constructor Used
Constructor Used
Constructor Used
Constructor Used
Constructor Used
Constructor Used
Constructor Used
Constructor Used
0
Destructor Used
Destructor Used
Destructor Used
Destructor Used
Destructor Used
Destructor Used
Destructor Used
Destructor Used
Destructor Used
Destructor Used
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ vim new_del.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/smart_pointer$ cd ..
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ mkdir fun_overloading
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ cd fun_overloading/
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ c++ sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ ./a.out 
30
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ c++ sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ ./a.out 
Adding two integers
30
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ c++ sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ ./a.out 
In function int a, float b
Adding two integers
30
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ nm sample.cpp 
nm: sample.cpp: File format not recognized
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ nm a.out 
0000000000201010 B __bss_start
0000000000201130 b completed.7696
                 U __cxa_atexit@@GLIBC_2.2.5
                 w __cxa_finalize@@GLIBC_2.2.5
0000000000201000 D __data_start
0000000000201000 W data_start
0000000000000830 t deregister_tm_clones
00000000000008c0 t __do_global_dtors_aux
0000000000200d80 t __do_global_dtors_aux_fini_array_entry
0000000000201008 D __dso_handle
0000000000200d88 d _DYNAMIC
0000000000201010 D _edata
0000000000201138 B _end
0000000000000af4 T _fini
0000000000000900 t frame_dummy
0000000000200d70 t __frame_dummy_init_array_entry
0000000000000d44 r __FRAME_END__
0000000000200f88 d _GLOBAL_OFFSET_TABLE_
0000000000000a66 t _GLOBAL__sub_I__Z3addii
                 w __gmon_start__
0000000000000b3c r __GNU_EH_FRAME_HDR
0000000000000778 T _init
0000000000200d80 t __init_array_end
0000000000200d70 t __init_array_start
0000000000000b00 R _IO_stdin_used
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
0000000000000af0 T __libc_csu_fini
0000000000000a80 T __libc_csu_init
                 U __libc_start_main@@GLIBC_2.2.5
000000000000099f T main
0000000000000870 t register_tm_clones
0000000000000800 T _start
0000000000201010 D __TMC_END__
000000000000094a T _Z3addff
0000000000000964 T _Z3addif
000000000000090a T _Z3addii
0000000000000a1d t _Z41__static_initialization_and_destruction_0ii
                 U _ZNSolsEi@@GLIBCXX_3.4
                 U _ZNSolsEPFRSoS_E@@GLIBCXX_3.4
                 U _ZNSt8ios_base4InitC1Ev@@GLIBCXX_3.4
                 U _ZNSt8ios_base4InitD1Ev@@GLIBCXX_3.4
0000000000201020 B _ZSt4cout@@GLIBCXX_3.4
                 U _ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@@GLIBCXX_3.4
0000000000000b04 r _ZStL19piecewise_construct
0000000000201131 b _ZStL8__ioinit
                 U _ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@@GLIBCXX_3.4
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ nm a.out | grep add
0000000000000a66 t _GLOBAL__sub_I__Z3addii
000000000000094a T _Z3addff
0000000000000964 T _Z3addif
000000000000090a T _Z3addii
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ c++ sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ nm a.out | grep add
0000000000000aa3 t _GLOBAL__sub_I__Z3addii
000000000000094a T _Z3addcc
0000000000000987 T _Z3addff
00000000000009a1 T _Z3addif
000000000000090a T _Z3addii
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/fun_overloading$ cd ../
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ mkdir default_args
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ cd default_args/
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ c++ sample.cpp 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ ./a.out 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ c++ sample.cpp 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ ./a.out 
RamB.TechIndian
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ c++ sample.cpp 
sample.cpp: In function 'int main()':
sample.cpp:22:17: error: too few arguments to function 'void fill_form(std::__cxx11::string, std::__cxx11::string, std::__cxx11::string)'
  fill_form("Ram");
                 ^
sample.cpp:13:6: note: declared here
 void fill_form(string name, string degree, string nationality)
      ^~~~~~~~~
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ c++ sample.cpp 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ ./a.out 
RamB.TechIndian
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ c++ sample.cpp 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ ./a.out 
DavidM.TechUS
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ c++ sample.cpp 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ ./a.out 
DavidM.TechUS
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/default_args$ cd ../
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ mkdir string
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ cd string
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ cd string
-bash: cd: string: No such file or directory
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ c++ sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ ./a.out 
Ram
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ c++ sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ ./a.out 
Ram gopal
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ c++ sample.cpp
sample.cpp: In function 'int main()':
sample.cpp:7:2: error: expected ',' or ';' before 'string'
  string search_name = " gopal";
  ^~~~~~
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ vim sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ c++ sample.cpp
sample.cpp: In function 'int main()':
sample.cpp:8:2: error: expected ',' or ';' before 'string'
  string search_name = " gopal";
  ^~~~~~
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ vim sample.cpp +8
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ c++ sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ ./a.out 
ram
akram
chandu
sri
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ vim sample.cpp +8
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ c++ sample.cpp
sample.cpp: In function 'int main()':
sample.cpp:13:7: error: 'name' was not declared in this scope
   if (name[i] == search_name)
       ^~~~
sample.cpp:13:7: note: suggested alternative: 'names'
   if (name[i] == search_name)
       ^~~~
       names
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ vim sample.cpp +8
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ c++ sample.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ ./a.out 
ram
akram
Name is found
chandu
sri
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ vim sample.cpp +8
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/string$ cd ..
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ mkdir memory_management
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp$ cd memory_management/
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
new_delete.cpp:13:2: error: expected ';' after class definition
 }
  ^
  ;
new_delete.cpp: In function 'int main()':
new_delete.cpp:17:28: error: no matching function for call to 'stu::stu(int)'
  stu *students = new stu(10);
                            ^
new_delete.cpp:5:3: note: candidate: stu::stu()
   stu()
   ^~~
new_delete.cpp:5:3: note:   candidate expects 0 arguments, 1 provided
new_delete.cpp:3:7: note: candidate: constexpr stu::stu(const stu&)
 class stu {
       ^~~
new_delete.cpp:3:7: note:   no known conversion for argument 1 from 'int' to 'const stu&'
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
new_delete.cpp: In function 'int main()':
new_delete.cpp:17:28: error: no matching function for call to 'stu::stu(int)'
  stu *students = new stu(10);
                            ^
new_delete.cpp:5:3: note: candidate: stu::stu()
   stu()
   ^~~
new_delete.cpp:5:3: note:   candidate expects 0 arguments, 1 provided
new_delete.cpp:3:7: note: candidate: constexpr stu::stu(const stu&)
 class stu {
       ^~~
new_delete.cpp:3:7: note:   no known conversion for argument 1 from 'int' to 'const stu&'
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +17
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ ./a.out 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
End of the program
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ valgrind ./a.out 
==18478== Memcheck, a memory error detector
==18478== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==18478== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==18478== Command: ./a.out
==18478== 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
End of the program
==18478== 
==18478== HEAP SUMMARY:
==18478==     in use at exit: 18 bytes in 1 blocks
==18478==   total heap usage: 3 allocs, 2 frees, 73,746 bytes allocated
==18478== 
==18478== LEAK SUMMARY:
==18478==    definitely lost: 18 bytes in 1 blocks
==18478==    indirectly lost: 0 bytes in 0 blocks
==18478==      possibly lost: 0 bytes in 0 blocks
==18478==    still reachable: 0 bytes in 0 blocks
==18478==         suppressed: 0 bytes in 0 blocks
==18478== Rerun with --leak-check=full to see details of leaked memory
==18478== 
==18478== For counts of detected and suppressed errors, rerun with: -v
==18478== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
new_delete.cpp: In function 'int main()':
new_delete.cpp:19:15: error: expected primary-expression before ';' token
  delete [] stu;
               ^
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
new_delete.cpp: In function 'int main()':
new_delete.cpp:19:14: error: expected primary-expression before ';' token
  delete[] stu;
              ^
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
new_delete.cpp: In function 'int main()':
new_delete.cpp:19:19: error: expected '}' at end of input
  delete[] students;
                   ^
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
new_delete.cpp: In function 'int main()':
new_delete.cpp:19:20: error: expected primary-expression before ']' token
  delete[] students[];
                    ^
new_delete.cpp:19:21: error: expected '}' at end of input
  delete[] students[];
                     ^
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
new_delete.cpp: In function 'int main()':
new_delete.cpp:19:17: error: expected '}' at end of input
  delete students;
                 ^
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ ./a.out 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
End of the program
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++  new_delete.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ ./a.out 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
End of the program
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ new_delete.cpp 
new_delete.cpp: In function 'void fun()':
new_delete.cpp:17:2: error: 'obj1' was not declared in this scope
  obj1 stu;
  ^~~~
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ new_delete.cpp 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ ./a.out 
Constructor  is called 
Destrictor is called 
End of the program
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ new_delete.cpp 
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ ./a.out 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Constructor  is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
Destrictor is called 
End of the program
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim new_delete.cpp +13
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ unique.cpp
unique.cpp: In function 'int main()':
unique.cpp:21:7: error: 'unique_ptr' is not a member of 'std'
  std::unique_ptr <stud > ptr (new stud);
       ^~~~~~~~~~
unique.cpp:21:24: error: expected primary-expression before '>' token
  std::unique_ptr <stud > ptr (new stud);
                        ^
unique.cpp:21:26: error: 'ptr' was not declared in this scope
  std::unique_ptr <stud > ptr (new stud);
                          ^~~
unique.cpp:21:26: note: suggested alternative: 'putw'
  std::unique_ptr <stud > ptr (new stud);
                          ^~~
                          putw
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ unique.cpp
unique.cpp: In function 'int main()':
unique.cpp:21:2: error: 'unique_ptr' was not declared in this scope
  unique_ptr <stud > ptr (new stud);
  ^~~~~~~~~~
unique.cpp:21:19: error: expected primary-expression before '>' token
  unique_ptr <stud > ptr (new stud);
                   ^
unique.cpp:21:21: error: 'ptr' was not declared in this scope
  unique_ptr <stud > ptr (new stud);
                     ^~~
unique.cpp:21:21: note: suggested alternative: 'putw'
  unique_ptr <stud > ptr (new stud);
                     ^~~
                     putw
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ ./a.out 
Constructor Used
End of the program
Destructor Used
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ ./a.out 
Constructor Used
End of the program
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ valgrind ./a.out 
==18611== Memcheck, a memory error detector
==18611== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==18611== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==18611== Command: ./a.out
==18611== 
Constructor Used
End of the program
==18611== 
==18611== HEAP SUMMARY:
==18611==     in use at exit: 4 bytes in 1 blocks
==18611==   total heap usage: 3 allocs, 2 frees, 73,732 bytes allocated
==18611== 
==18611== LEAK SUMMARY:
==18611==    definitely lost: 4 bytes in 1 blocks
==18611==    indirectly lost: 0 bytes in 0 blocks
==18611==      possibly lost: 0 bytes in 0 blocks
==18611==    still reachable: 0 bytes in 0 blocks
==18611==         suppressed: 0 bytes in 0 blocks
==18611== Rerun with --leak-check=full to see details of leaked memory
==18611== 
==18611== For counts of detected and suppressed errors, rerun with: -v
==18611== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ ./a.out 
Constructor Used
End of the program
Destructor Used
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ valgrind ./a.out 
==18619== Memcheck, a memory error detector
==18619== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==18619== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==18619== Command: ./a.out
==18619== 
Constructor Used
End of the program
Destructor Used
==18619== 
==18619== HEAP SUMMARY:
==18619==     in use at exit: 0 bytes in 0 blocks
==18619==   total heap usage: 3 allocs, 3 frees, 73,732 bytes allocated
==18619== 
==18619== All heap blocks were freed -- no leaks are possible
==18619== 
==18619== For counts of detected and suppressed errors, rerun with: -v
==18619== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ valgrind ./a.out 
==18624== Memcheck, a memory error detector
==18624== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==18624== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==18624== Command: ./a.out
==18624== 
Constructor Used
End of the program
Destructor Used
==18624== 
==18624== HEAP SUMMARY:
==18624==     in use at exit: 0 bytes in 0 blocks
==18624==   total heap usage: 3 allocs, 3 frees, 73,732 bytes allocated
==18624== 
==18624== All heap blocks were freed -- no leaks are possible
==18624== 
==18624== For counts of detected and suppressed errors, rerun with: -v
==18624== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ vim unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ c++ unique.cpp
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ valgrind ./a.out 
==18631== Memcheck, a memory error detector
==18631== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==18631== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==18631== Command: ./a.out
==18631== 
Constructor Used
End of the program
==18631== 
==18631== HEAP SUMMARY:
==18631==     in use at exit: 4 bytes in 1 blocks
==18631==   total heap usage: 3 allocs, 2 frees, 73,732 bytes allocated
==18631== 
==18631== LEAK SUMMARY:
==18631==    definitely lost: 4 bytes in 1 blocks
==18631==    indirectly lost: 0 bytes in 0 blocks
==18631==      possibly lost: 0 bytes in 0 blocks
==18631==    still reachable: 0 bytes in 0 blocks
==18631==         suppressed: 0 bytes in 0 blocks
==18631== Rerun with --leak-check=full to see details of leaked memory
==18631== 
==18631== For counts of detected and suppressed errors, rerun with: -v
==18631== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
kamal@kamal-VirtualBox:~/AptComputingAcademy/Cpp/memory_management$ packet_write_wait: Connection to 192.168.43.26 port 22: Broken pipe
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ ipython
Python 3.7.2 (default, Jan 13 2019, 12:50:15) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import is                                                                              
  File "<ipython-input-1-b3777eb89c38>", line 1
    import is
            ^
SyntaxError: invalid syntax


In [2]: import os                                                                              

In [3]: os.getcwd()                                                                            
Out[3]: '/Users/kamalmukiri/Documents/AptComputingAcademy/Python/Projects/web_scrapping'

In [4]: os.listdir()                                                                           
Out[4]: ['get_scricket_score.py']

In [5]: os.stat('get_scricket_score.py')                                                       
Out[5]: os.stat_result(st_mode=33188, st_ino=11199728, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=484, st_atime=1552453405, st_mtime=1552372567, st_ctime=1552372567)

In [6]: quit                                                                                   

Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ pwd
/Users/kamalmukiri/Documents/AptComputingAcademy/Python/Projects/web_scrapping
Kamals-MacBook-Air:web_scrapping kamalmukiri$ 
Kamals-MacBook-Air:web_scrapping kamalmukiri$ cd ../../
Kamals-MacBook-Air:Python kamalmukiri$ 
Kamals-MacBook-Air:Python kamalmukiri$ ls
Assessments			PythonCourseScreenVideoRecords
Books				SmartDict
Classes				Untitled.ipynb
DataFrames			Untitled1.ipynb
GreatLearning_Courses		cython
JupyterNotebooks		final.py
PYE040219			numpy
PYM171218_Modules		pylint
Programs			sample.py
Projects			sample.py.txt
PyCharmProject01		testing
PythonAndIoT_CourseDetails.pdf	tkinter
PythonCourseDetails.odp		utils
PythonCourseDetails.pdf		web_scrapping
Kamals-MacBook-Air:Python kamalmukiri$ pwd
/Users/kamalmukiri/Documents/AptComputingAcademy/Python
Kamals-MacBook-Air:Python kamalmukiri$ 
Kamals-MacBook-Air:Python kamalmukiri$ 
Kamals-MacBook-Air:Python kamalmukiri$ 
Kamals-MacBook-Air:Python kamalmukiri$ vim line_count.py
Kamals-MacBook-Air:Python kamalmukiri$ pwd
/Users/kamalmukiri/Documents/AptComputingAcademy/Python
Kamals-MacBook-Air:Python kamalmukiri$ python3 LocCount.py 
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Python/Classes/Classes/FileHandling/venv/lib/python3.7/site-packages/xlwt/BIFFRecords.py
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Python/Classes/Classes/FileHandling/venv/lib/python3.7/site-packages/xlwt/UnicodeUtils.py
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Trash/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l4xx.h
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Trash/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l476xx.h
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/IoT/Projects/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l4xx.h
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/IoT/Projects/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l476xx.h
No of lines of c = 6858150 
Calculated in 17.89636993408203secs
Traceback (most recent call last):
  File "LocCount.py", line 78, in <module>
    log_prev_fd = open("LogPrev.txt", 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'LogPrev.txt'
Kamals-MacBook-Air:Python kamalmukiri$ pwd
/Users/kamalmukiri/Documents/AptComputingAcademy/Python
Kamals-MacBook-Air:Python kamalmukiri$ vim Lo
LocCount.py     LogPresent.txt  
Kamals-MacBook-Air:Python kamalmukiri$ vim LocCount.py 
Kamals-MacBook-Air:Python kamalmukiri$ vim LocCount.py 
Kamals-MacBook-Air:Python kamalmukiri$ python3 LocCount.py 
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Python/Classes/Classes/FileHandling/venv/lib/python3.7/site-packages/xlwt/BIFFRecords.py
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Python/Classes/Classes/FileHandling/venv/lib/python3.7/site-packages/xlwt/UnicodeUtils.py
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Trash/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l4xx.h
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Trash/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l476xx.h
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/IoT/Projects/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l4xx.h
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/IoT/Projects/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l476xx.h
No of lines of c = 6858154 
Calculated in 17.86015295982361secs
Difference between present and previous stats:
******************
  {'/Users/kamalmukiri/Documents/AptComputingAcademy/Python/LocCount.py:73\n'}
*********************
Kamals-MacBook-Air:Python kamalmukiri$ python3 LocCount.py 
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Python/Classes/Classes/FileHandling/venv/lib/python3.7/site-packages/xlwt/BIFFRecords.py
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Python/Classes/Classes/FileHandling/venv/lib/python3.7/site-packages/xlwt/UnicodeUtils.py
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Trash/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l4xx.h
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/Trash/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l476xx.h
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/IoT/Projects/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l4xx.h
Exception File name =  /Users/kamalmukiri/Documents/AptComputingAcademy/IoT/Projects/SmartFarming/STM32_Practices/Project01_WithTwoUSART/Drivers/CMSIS/Device/ST/STM32L4xx/Include/stm32l476xx.h
No of lines of c = 6858154 
Calculated in 21.74770474433899secs
Difference between present and previous stats:
******************
  set()
*********************
Kamals-MacBook-Air:Python kamalmukiri$ vim Lo
LocCount.py     LogPresent.txt  LogPrev.txt     
Kamals-MacBook-Air:Python kamalmukiri$ vim Lo
LocCount.py     LogPresent.txt  LogPrev.txt     
Kamals-MacBook-Air:Python kamalmukiri$ vim LogPrev.txt 
Kamals-MacBook-Air:Python kamalmukiri$ vim LocCount.py 

    return

if __name__ == "__main__":
    try:
        os.rename("LogPresent.txt", "LogPrev.txt")
    except:
        pass

    num_lines = 0
    with open("LogPresent.txt", 'w') as log_fd:
        Log_fd = log_fd
        start = time.time()
        count_c_code(ROOT_DIR)
        end = time.time()
        print("No of lines of c = {} \nCalculated in {}secs".format(num_lines, end-start))
    try:
        log_present_fd = open("LogPresent.txt", 'r')
        log_present_lines = set(log_present_fd.readlines())
        log_present_fd.close()
        log_prev_fd = open("LogPrev.txt", 'r')
        log_prev_lines = set(log_prev_fd.readlines())
        log_prev_fd.close()
    except (FileNotFoundError):
        print("There is no backup data")

    else:
        print("Difference between present and previous stats:\n******************\n ", log_present_lines - log_prev_lines)
        print("*********************")
