Author:
CrackNotMe
Language:
C/C++
Platform:
Windows

https://crackmes.one/crackme/6989ed7dfb46458f1ef6cee4
Difficulty:
4.0 

Проводим первичный осмотр:
Заходим в strings, наблюдаем, что строки зашифрованы, нет password, ничего. Хотя видно, что есть два странных парента, и setthreadcontext failed, значит где-то перезапись регистров для какого-то потока есть.
<img width="1509" height="822" alt="image" src="https://github.com/user-attachments/assets/fd67844d-dc75-4530-ab6c-c32057d83129" />

дальше переходим в импорты. Видим, что в User32 у нас находится вывод какого-то сообщения, запоминаем. 

<img width="1507" height="849" alt="image" src="https://github.com/user-attachments/assets/964b1b81-d92b-4c14-b2ce-432931228f9f" />


0000000140025038		GetCurrentThread	KERNEL32
0000000140025040		CreateProcessA	KERNEL32
0000000140025048		GetThreadContext	KERNEL32
0000000140025050		SetThreadContext	KERNEL32
0000000140025058		ReadProcessMemory	KERNEL32
0000000140025060		GetModuleFileNameA	KERNEL32


Можем тут увидеть во такую интересную последовательность, но запоминаем их, дальше будет разбирать. 
Переходим в мейн, быстро пробегаемся по коду. 
<img width="402" height="678" alt="image" src="https://github.com/user-attachments/assets/2bfa4488-cff2-465f-bd82-25380e49e730" />
видим какую-то манипуляцию со строкой и выводом --child 

В конце видим две развилки: 
00000001400069EC                 jmp     sub_140004D00
00000001400069F1                 call    sub_140005490
<img width="572" height="227" alt="image" src="https://github.com/user-attachments/assets/a6d519a6-fd1f-4ec3-a1ed-d0b0e8f04575" />

Но от чего они зависят?
Я решил узнать через x64dbg, делаем
bp CrackMe.exe+68C4
Видим, что cmp у нас будет 01, сравнивая с 1, в общем, прыжок будет. 
В ida смотрим псевдокод. 
v3 = 0;
  if ( argc <= 1 )
  {
    v5 = v15;
    v4 = (__int64)Block[0];
LABEL_8:
    v10 = 0;
    goto LABEL_9;
  }
  Block[1] = 0;
  v15 = 15;
  v14 = 7;
  Block[0] = (void *)0x646C6968632D2DLL;
  v3 = 3;
  v4 = 0x646C6968632D2DLL;
  v5 = 15;
  v6 = argv[1];
  v7 = (char *)((char *)Block - v6);
  do
  {
    v8 = (unsigned __int8)v7[(_QWORD)v6];
    v9 = *(unsigned __int8 *)v6 - v8;
    if ( v9 )
      break;
    ++v6;
  }
  В котором видим, что у нас есть 2 агрумента.
  v6 = argv[1];
    if ( argc <= 1 )

  Проверим теорию, проверим где выводится --child
  mov     [rbp+var_10], 7 проверка длинны --child как видим тут 7 символов. и это видно в v14 = 7, так же видим что  v15 = 15; 15 символов, это дальше увидим в разборе - это я чуть позже пишу. 
  0x646C6968632D2DLL - у нас будет --child. 
  Собираем строку
  

Давайте быстро проверим первый путь 
00000001400069EC                 jmp     sub_140004D00

интересная функция, зачем нам в р15 добавлять такое число? 
0000000140004EF9                 mov     r15, 0B3E192F8A4D5C6B7h
<img width="373" height="103" alt="image" src="https://github.com/user-attachments/assets/a20e0c4c-7499-4cfa-b700-b6c0b740fbcc" />
Первичный осмотр, как по мне, выглядит как виртуальнаямашина, знакомая мне по 3 лвлу, но преждевременно тяжело сказать.

Но идём ко второй развилке 
00000001400069F1                 call    sub_140005490

Тут мы сразу же видим, нашу ту ошибку: 
<img width="558" height="283" alt="image" src="https://github.com/user-attachments/assets/e961226d-c75f-4f5f-b6c7-86f51ba12cc1" />

И самое главное:
<img width="1138" height="805" alt="image" src="https://github.com/user-attachments/assets/3a226e82-3d8f-4f34-a84f-c36fa9aeb56f" />

мы можем наблюдать:
text:00000001400058D5                 call    cs:CreateProcessA 

Мы создаём какой-то процесс, сначала углубляться не буду, простите. , но после создания, у нас нас, видим есть прыжок дальше или переход на ошибку, если мы прыгаем, то мы минуем ошибку. 
<img width="1195" height="551" alt="image" src="https://github.com/user-attachments/assets/7c09307b-d590-4990-a4dc-510d01a69cf5" />
и оказываемся здесь, где опять в rsi мы закидываем какое-то не понятно число 
:00000001400058FA                 mov     rsi, 9F2D38B17C6A4E5Fh
Но это одно из наблюдений. 
text:0000000140005910                 call    cs:WaitForDebugEvent 
Здесь мы ожидаем какое-то событие
Вообще вот так у нас должно выглядеть работа:
<img width="1250" height="832" alt="image" src="https://github.com/user-attachments/assets/0fc457fd-a66c-4b64-bea5-041e81af47b4" />

000000014000598B                 call    cs:GetThreadContext берём регистра процессора у какого-то потока, 

00000001400059CB                 call    cs:ReadProcessMemory читаем что-то 

00000001400059FC                 call    cs:SetThreadContext взяли байты у регистров процессора в прошлый раз, теперь вставляем. Вообще всё это напоминает нам виртуальную машину, но давайте уже запускать x64dbg

Ставим бряк на 5490 и 58d5, начало 2ого, так сказать, пути. 
Я неспеша жму ф8, чтобы наблюдать, что происходит и замечаю тут 
00007FF79142577A  | E8 01D0FFFF              | call <crackme.sub_7FF791422780>         | создаётся у нас в rbp-38 строка:"\"E:\\crackmes\\lv4\\CrackMe.exe\" --child"
Можно попробовать запустить, но пока не имеет значения, мы проходим к 
00007FF791425910  | FF15 0AF70100            | call qword ptr ds:[<WaitForDebugEvent>] |
тут долгие проверки, на 1, если не 1 цикл врубается
Значит брякаем 00007FF79142592D  | 81BD 90000000 03000080   | cmp dword ptr ss:[rbp+90],80000003      | 
Чтобы помочь нам самим, ничего интересного не нахожу решаю брякать всё подряд 
598B
59CB 
59FC
Потыкав ф8, я вижу тут 
<img width="1144" height="78" alt="image" src="https://github.com/user-attachments/assets/c7b68fbb-6ab8-49bc-a0c5-0f963f73daa8" />
Переходим по адресу тут у нас вот такая штучка, что значит она? Я ебу? 
.text:0000000140006A10                 xor     rax, rax
.text:0000000140006A13                 int     3               ; Trap to Debugger
.text:0000000140006A14                 retn

00007FF7914259DB  | 48:89B5 B8020000         | mov qword ptr ss:[rbp+2B8],rsi          | 9F2D38B17C6A4E5F перекидываем в память
00007FF7914259E2  | 80BD 40070000 CC         | cmp byte ptr ss:[rbp+740],CC            | сравниваем хз зачем с сс
Совершаем прыжок

59CB 
59FC

