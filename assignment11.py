drop function if exists alphanum; 
delimiter | 
create function alphanum( str char(255) ) returns char(255) deterministic
begin 
  declare i, len smallint default 1; 
  declare ret char(255) default ''; 
  declare c char(1); 
  set len = char_length( str ); 
  repeat 
    begin 
      set c = mid( str, i, 1 ); 
      if c regexp '[[:alnum:]]' then 
        set ret=concat(ret,c); 
      end if; 
      set i = i + 1; 
    end; 
  until i > len end repeat; 
  return ret; 
end | 
delimiter ; 
