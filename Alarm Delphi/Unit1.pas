unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, IdBaseComponent, IdComponent, IdTCPConnection,
  IdTCPClient, IdHTTP, ExtCtrls, ShellAPI, Menus, Registry,ShlObj;

  const  WM_ICONRESPONSE = WM_USER + 1;
  CSIDL_DESKTOP                       = $0000; { <desktop> }
  CSIDL_INTERNET                      = $0001; { Internet Explorer (icon on desktop) }
  CSIDL_PROGRAMS                      = $0002; { Start Menu\Programs }
  CSIDL_CONTROLS                      = $0003; { My Computer\Control Panel }
  CSIDL_PRINTERS                      = $0004; { My Computer\Printers }
  CSIDL_PERSONAL                      = $0005; { My Documents.  This is equivalent to CSIDL_MYDOCUMENTS in XP and above }
  CSIDL_FAVORITES                     = $0006; { <user name>\Favorites }
  CSIDL_STARTUP                       = $0007; { Start Menu\Programs\Startup }
  CSIDL_RECENT                        = $0008; { <user name>\Recent }
  CSIDL_SENDTO                        = $0009; { <user name>\SendTo }
  CSIDL_BITBUCKET                     = $000a; { <desktop>\Recycle Bin }
  CSIDL_STARTMENU                     = $000b; { <user name>\Start Menu }
  CSIDL_MYDOCUMENTS                   = $000c; { logical "My Documents" desktop icon }
  CSIDL_MYMUSIC                       = $000d; { "My Music" folder }
  CSIDL_MYVIDEO                       = $000e; { "My Video" folder }
  CSIDL_DESKTOPDIRECTORY              = $0010; { <user name>\Desktop }
  CSIDL_DRIVES                        = $0011; { My Computer }
  CSIDL_NETWORK                       = $0012; { Network Neighborhood (My Network Places) }
  CSIDL_NETHOOD                       = $0013; { <user name>\nethood }
  CSIDL_FONTS                         = $0014; { windows\fonts }
  CSIDL_TEMPLATES                     = $0015;
  CSIDL_COMMON_STARTMENU              = $0016; { All Users\Start Menu }
  CSIDL_COMMON_PROGRAMS               = $0017; { All Users\Start Menu\Programs }
  CSIDL_COMMON_STARTUP                = $0018; { All Users\Startup }
  CSIDL_COMMON_DESKTOPDIRECTORY       = $0019; { All Users\Desktop }
  CSIDL_APPDATA                       = $001a; { <user name>\Application Data }
  CSIDL_PRINTHOOD                     = $001b; { <user name>\PrintHood }
  CSIDL_LOCAL_APPDATA                 = $001c; { <user name>\Local Settings\Application Data (non roaming) }
  CSIDL_ALTSTARTUP                    = $001d; { non localized startup }
  CSIDL_COMMON_ALTSTARTUP             = $001e; { non localized common startup }
  CSIDL_COMMON_FAVORITES              = $001f;
  CSIDL_INTERNET_CACHE                = $0020;
  CSIDL_COOKIES                       = $0021;
  CSIDL_HISTORY                       = $0022;
  CSIDL_COMMON_APPDATA                = $0023; { All Users\Application Data }
  CSIDL_WINDOWS                       = $0024; { GetWindowsDirectory() }
  CSIDL_SYSTEM                        = $0025; { GetSystemDirectory() }
  CSIDL_PROGRAM_FILES                 = $0026; { C:\Program Files }
  CSIDL_MYPICTURES                    = $0027; { C:\Program Files\My Pictures }
  CSIDL_PROFILE                       = $0028; { USERPROFILE }
  CSIDL_SYSTEMX86                     = $0029; { x86 system directory on RISC }
  CSIDL_PROGRAM_FILESX86              = $002a; { x86 C:\Program Files on RISC }
  CSIDL_PROGRAM_FILES_COMMON          = $002b; { C:\Program Files\Common }
  CSIDL_PROGRAM_FILES_COMMONX86       = $002c; { x86 C:\Program Files\Common on RISC }
  CSIDL_COMMON_TEMPLATES              = $002d; { All Users\Templates }
  CSIDL_COMMON_DOCUMENTS              = $002e; { All Users\Documents }
  CSIDL_COMMON_ADMINTOOLS             = $002f; { All Users\Start Menu\Programs\Administrative Tools }
  CSIDL_ADMINTOOLS                    = $0030; { <user name>\Start Menu\Programs\Administrative Tools }
  CSIDL_CONNECTIONS                   = $0031; { Network and Dial-up Connections }
  CSIDL_COMMON_MUSIC                  = $0035; { All Users\My Music }
  CSIDL_COMMON_PICTURES               = $0036; { All Users\My Pictures }
  CSIDL_COMMON_VIDEO                  = $0037; { All Users\My Video }
  CSIDL_RESOURCES                     = $0038; { Resource Directory }
  CSIDL_RESOURCES_LOCALIZED           = $0039; { Localized Resource Directory }
  CSIDL_COMMON_OEM_LINKS              = $003a; { Links to All Users OEM specific apps }
  CSIDL_CDBURN_AREA                   = $003b; { USERPROFILE\Local Settings\Application Data\Microsoft\CD Burning }
  CSIDL_COMPUTERSNEARME               = $003d; { Computers Near Me (computered from Workgroup membership) }
  CSIDL_PROFILES                      = $003e;

  type
  thr = class(TThread)
  private
  public
   procedure Execute(); override;
  end;








  type
  Tfrm_main = class(TForm)
    Label1: TLabel;
    Edit1: TEdit;
    Label2: TLabel;
    Label3: TLabel;
    Edit2: TEdit;
    Button1: TButton;
    Edit3: TEdit;
    IdHTTP1: TIdHTTP;
    Edit4: TEdit;
    Edit5: TEdit;
    Timer1: TTimer;
    Timer2: TTimer;
    pmRightClick: TPopupMenu;
    N1: TMenuItem;
    RadioButton1: TRadioButton;
    RadioButton2: TRadioButton;
    procedure FormCreate(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
    procedure Timer2Timer(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure N1Click(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
    procedure Button1Click(Sender: TObject);
    procedure RadioButton1Click(Sender: TObject);
    procedure RadioButton2Click(Sender: TObject);

  private
    FIconShown: Boolean;
    FTrayIconData: TNotifyIconData;
    myReg: TRegistry;
    procedure HideTrayIcon;
    procedure IconResponse(var Msg: TMessage); message WM_ICONRESPONSE;

  public
    { Public declarations }
        procedure ShowTrayIcon;
  end;

var
  frm_main: Tfrm_main;
  is_checking:boolean;

implementation

uses Unit2;

{$R *.dfm}

 procedure RunOnStartup(const sCmdLine: string; bRunOnce: boolean = false; Remove: Boolean = false) ;
 var
   sKey: string;
   Section: string;
 const
   ApplicationTitle = 'ÕäÇíÚ ÝæáÇÏ ÝÑÎÔåÑ';
 begin
   if (bRunOnce) then
     sKey := 'Once'
   else
     sKey := '';
 
   Section := 'Software\Microsoft\Windows\CurrentVersion\Run' + sKey + #0;
 
   with TRegIniFile.Create('') do
     try
       RootKey := HKEY_LOCAL_MACHINE;
       if Remove then
         DeleteKey(Section, ApplicationTitle)
       else
         WriteString(Section, ApplicationTitle, sCmdLine) ;
     finally
       Free;
     end;
 end;




function GetSpecialFolderPath(Folder: Integer; CanCreate: Boolean): string;

// Gets path of special system folders
//
// Call this routine as follows:
// GetSpecialFolderPath (CSIDL_PERSONAL, false)
//        returns folder as result
//
var
   FilePath: array [0..255] of char;

begin
 SHGetSpecialFolderPath(0, @FilePath[0], FOLDER, CanCreate);
 Result := FilePath;
end;



procedure Tfrm_main.FormCreate(Sender: TObject);
begin

 try
myReg := TRegistry.Create;
myReg.RootKey := HKEY_LOCAL_MACHINE;
if myReg.OpenKey('SOFTWARE\FSI\', FALSE) then
begin

edit1.Text:=myReg.ReadString('edit1');
edit2.Text:=myReg.ReadString('edit2');
edit3.Text:=myReg.ReadString('edit3');
edit4.Text:=myReg.ReadString('edit4');
edit5.Text:=myReg.ReadString('edit5');

end;
 finally
myReg.Free;
hide;
 end;




ShowTrayIcon;



end;


  procedure Tfrm_main.ShowTrayIcon;
  begin
    if not FIconShown then
    begin
      with FTrayIconData do
      begin
        uID := 1;
        Wnd := Handle;
        cbSize := SizeOf(FTrayIconData);
        hIcon := Application.Icon.Handle;
        uCallbackMessage := WM_ICONRESPONSE;
        uFlags := NIF_TIP + NIF_MESSAGE + NIF_ICON;
        StrPCopy(szTip, 'ÓíÓÊã íÛÇã ÏåäÏå í ÇÊæãÇÓíæä ÕäÇíÚ ÝæáÇÏ ÝÑÎÔåÑ');
      end;
      Shell_NotifyIcon(NIM_ADD, @FTrayIconData);
      FIconShown := True;
    end;
  end;

  procedure Tfrm_main.HideTrayIcon;
  begin
    if FIconShown then
    begin
      Shell_NotifyIcon(NIM_DELETE, @FTrayIconData);
      FIconShown := False;
    end;
  end;


procedure Tfrm_main.Timer1Timer(Sender: TObject);
var
  InputStringList,param : TStringList;
  st1,st2 : TStringStream;
  url : string;
begin


st1 := TStringStream.Create('uname='+edit1.text+'&pass='+edit2.text);
st2 := TStringStream.Create('');
url := 'http://'+edit3.text+':'+edit4.text+Edit5.Text+'/py_listener.py';
IdHttp1.Request.Accept := '*/*';
IdHTTP1.Request.Connection := 'Keep-Alive';
IdHttp1.Request.ContentType := 'application/x-www-form-urlencoded';

try
  IdHTTP1.Post(url,st1,st2);
except
  form2.Label1.Caption:='ÚÏã ÇÑÊÈÇØ ÈÇ ÓÑæÑ';
  form2.Show;
  exit;
end;
  form2.Label1.Caption:='˜ÇÑÈÑ ãÍÊÑã - ÏÑ ˜ÇÑÊÇÈá ÔãÇ äÇãå ( åÇí ) ÌÏíÏí ÏÑíÇÝÊ ÑÏíÏå ÇÓÊ. áØÝÇ Èå ÓÇíÊ ÇÊæãÇÓíæä ãÑÇÌÚå æ äÇãå åÇí ÏÑíÇÝÊí ÑÇ ííÑí ÝÑãÇííÏ - ÈÇ ÊÔ˜Ñ - æÇÍÏ IT';
if strtoint(copy(st2.DataString,0,1)) > 0 then
begin
  form2.Show;
end;
if strtoint(copy(st2.DataString,0,1)) = 0 then
begin
  form2.Hide;
end;

end;

procedure Tfrm_main.IconResponse(var Msg: TMessage);

   var
    pt: TPoint;
  begin
    case Msg.lParam of
      WM_LBUTTONDOWN:
      begin
        // Do nothing
      end;
      WM_RBUTTONDOWN:
      begin
        GetCursorPos(pt);
        pmRightClick.Popup(pt.x, pt.y);
      end;
    end;
end;
procedure Tfrm_main.Timer2Timer(Sender: TObject);
begin
 //   ShowTrayIcon;
 frm_main.Hide;
    Timer2.Enabled:=false;
end;

procedure Tfrm_main.FormDestroy(Sender: TObject);
begin
  HideTrayIcon;
end;

procedure Tfrm_main.N1Click(Sender: TObject);
begin
frm_main.Show;
end;

procedure Tfrm_main.FormClose(Sender: TObject; var Action: TCloseAction);
begin
hide();
Action := caNone;
end;



procedure thr.Execute;
begin

    //
end;


procedure Tfrm_main.Button1Click(Sender: TObject);
begin
 try
myReg := TRegistry.Create;
myReg.RootKey := HKEY_LOCAL_MACHINE;
if myReg.OpenKey('SOFTWARE\FSI\', TRUE) then
begin
myReg.WriteString('edit1', Edit1.Text);
myReg.WriteString('edit2', Edit2.Text);
myReg.WriteString('edit3', Edit3.Text);
myReg.WriteString('edit4', Edit4.Text);
myReg.WriteString('edit5', Edit5.Text);

CopyFile(pansichar(Application.ExeName),pansichar(GetSpecialFolderPath(CSIDL_STARTUP,true)+'\fsichecker.exe'),false);
//RunOnStartup('c:\fsichecker.exe',false,false);
//Hide;
end;
 finally
myReg.Free;
hide;
 end;

end;

procedure Tfrm_main.RadioButton1Click(Sender: TObject);
begin

edit3.Text:='192.168.0.105';
edit4.Text:='80';

end;

procedure Tfrm_main.RadioButton2Click(Sender: TObject);
begin
edit3.Text:='91.98.234.104';
edit4.Text:='91';

end;

end.
