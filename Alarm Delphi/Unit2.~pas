unit Unit2;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls;

type
  TForm2 = class(TForm)
    Label1: TLabel;
    Shape1: TShape;
    Timer1: TTimer;

    procedure Timer1Timer(Sender: TObject);
  private

  
  public
    { Public declarations }

  end;

var
  Form2: TForm2;
      asdfasdf:integer;

implementation

uses Unit1;

{$R *.dfm}

procedure TForm2.Timer1Timer(Sender: TObject);
begin
if asdfasdf=0 then Shape1.Brush.Color  := $00E8E8FF else Shape1.Brush.Color  := clWhite;
if asdfasdf=0 then  asdfasdf:=1 else asdfasdf:=0;
form2.Left := Screen.Width-form2.Width;
form2.top := Screen.Height-form2.Height-40;

end;

end.
