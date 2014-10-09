# -*- coding: utf-8 -*-

'''
Copyright (C) 2014                                                     

This program is free software: you can redistribute it and/or modify   
it under the terms of the GNU General Public License as published by   
the Free Software Foundation, either version 3 of the License, or      
(at your option) any later version.                                    

This program is distributed in the hope that it will be useful,        
but WITHOUT ANY WARRANTY; without even the implied warranty of         
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
GNU General Public License for more details.                           

You should have received a copy of the GNU General Public License      
along with this program. If not, see <http://www.gnu.org/licenses/  
'''                                                                      

import urllib,urllib2,re,xbmc,xbmcplugin,xbmcgui

base_url = 'http://phim3s.net/'
pagestr = map(str, range(1,200))

def CATEGORIES():
        addDir('[COLOR red]Tìm Kiếm Phim[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR yellow]Search[/COLOR]','http://phim3s.net',1,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR lime]Phim Hồng Kông[/COLOR]','http://phim3s.net/quoc-gia/phim-hong-kong',2,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR magenta]Phim Hàn Quốc[/COLOR]','http://phim3s.net/quoc-gia/phim-han-quoc',3,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR yellow]Phim Việt Nam[/COLOR]','http://phim3s.net/quoc-gia/phim-viet-nam/',4,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR blue]Phim Trung Quốc[/COLOR]','http://phim3s.net/quoc-gia/phim-trung-quoc/',6,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR red]Phim Thái Lan[/COLOR]','http://phim3s.net/quoc-gia/phim-thai-lan/',7,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR lime]Phim Mỹ  - Movies & TV Series[/COLOR]','http://phim3s.net/quoc-gia/phim-my/',21,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR blue]Phim Mới * Phim Chiếu Rạp[/COLOR]','http://phim3s.net/danh-sach/phim-chieu-rap',5,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR magenta]Phim Hành Động[/COLOR]','http://phim3s.net/the-loai/phim-hanh-dong/',8,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR yellow]Phim Võ Thuật[/COLOR]','http://phim3s.net/the-loai/phim-vo-thuat/',9,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR blue]Phim Tâm Lý [/COLOR]','http://phim3s.net/the-loai/phim-tam-ly/',10,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR lime]Phim Hài Hước[/COLOR]','http://phim3s.net/the-loai/phim-hai-huoc/',11,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR red]Phim Kinh Dị[/COLOR]','http://phim3s.net/the-loai/phim-kinh-di/',13,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR blue]Phim Hình Sự[/COLOR]','http://phim3s.net/the-loai/phim-hinh-su/',14,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR yellow]Phim Chiến Tranh[/COLOR]','http://phim3s.net/the-loai/phim-chien-tranh/',15,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR red]Phim Thần Thoại[/COLOR]','http://phim3s.net/the-loai/phim-than-thoai/',18,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR lime]Phim Viễn Tưởng[/COLOR]','http://phim3s.net/the-loai/phim-vien-tuong/',19,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR magenta]Phim Cổ Trang[/COLOR]','http://phim3s.net/the-loai/phim-co-trang/',20,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        addDir('[COLOR blue]Phim Phiêu Lưu[/COLOR]','http://phim3s.net/the-loai/phim-phieu-luu/',12,'http://fs04.androidpit.info/a/a2/27/phim3s-a22795-w144.png')
        
def SEARCH():
    try: 
        keyb = xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
        keyb.doModal()
        if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText())
        url = 'http://phim3s.net/search?keyword='+searchText
        INDEX(url)
    except: pass
		
def SUBCATEGORIES_HongKong():
		i=0
		for i in range(13):
			addDir('[COLOR red]Trang ' + pagestr[i] + '[/COLOR][COLOR lime] - Phim Hồng Kông[/COLOR]','http://phim3s.net/quoc-gia/phim-hong-kong/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
		
def SUBCATEGORIES_RAP():	
		i=0
		for i in range(22):		
			addDir('[COLOR blue]Trang ' + pagestr[i] + '[/COLOR][COLOR lime] - Phim Mới * Phim Chiếu Rạp [/COLOR]','http://phim3s.net/danh-sach/phim-chieu-rap/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
 		
def SUBCATEGORIES_VietNam():
		i=0
		for i in range(17):
			addDir('[COLOR blue]Trang ' + pagestr[i] + '[/COLOR][COLOR yellow] - Phim Việt Nam [/COLOR]','http://phim3s.net/quoc-gia/phim-viet-nam/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
			
def SUBCATEGORIES_HANQUOC():
		i=0
		for i in range(19):
			addDir('[COLOR green]Trang ' + pagestr[i] + '[/COLOR][COLOR magenta] - Phim Hàn Quốc [/COLOR]','http://phim3s.net/quoc-gia/phim-han-quoc/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1

def SUBCATEGORIES_TrungQuoc():
		i=0
		for i in range(27):
			addDir('[COLOR magenta]Trang ' + pagestr[i] + '[/COLOR][COLOR blue] - Phim Trung Quốc [/COLOR]','http://phim3s.net/quoc-gia/phim-trung-quoc/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
			
def SUBCATEGORIES_ThaiLan():
		i=0
		for i in range(3):
			addDir('[COLOR yellow]Trang ' + pagestr[i] + '[/COLOR][COLOR red] - Phim Thái Lan [/COLOR]','http://phim3s.net/quoc-gia/phim-thai-lan/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
			
def SUBCATEGORIES_HanhDong():
		i=0
		for i in range(57):
			addDir('[COLOR red]Trang ' + pagestr[i] + '[/COLOR][COLOR lime] - Phim Hành Động[/COLOR]','http://phim3s.net/the-loai/phim-hanh-dong/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
		
def SUBCATEGORIES_VoThuat():	
		i=0
		for i in range(20):		
			addDir('[COLOR blue]Trang ' + pagestr[i] + '[/COLOR][COLOR lime] - Phim Võ Thuật [/COLOR]','http://phim3s.net/the-loai/phim-vo-thuat/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
 		
def SUBCATEGORIES_TamLy():
		i=0
		for i in range(68):
			addDir('[COLOR blue]Trang ' + pagestr[i] + '[/COLOR][COLOR yellow] - Phim Tâm Lý [/COLOR]','http://phim3s.net/the-loai/phim-tam-ly/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
			
def SUBCATEGORIES_HaiHuoc():
		i=0
		for i in range(47):
			addDir('[COLOR green]Trang ' + pagestr[i] + '[/COLOR][COLOR magenta] - Phim Hài Hước[/COLOR]','http://phim3s.net/the-loai/phim-hai-huoc/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1

def SUBCATEGORIES_KinhDi():
		i=0
		for i in range(21):
			addDir('[COLOR magenta]Trang ' + pagestr[i] + '[/COLOR][COLOR blue] - Phim Kinh Dị [/COLOR]','http://phim3s.net/the-loai/phim-kinh-di/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
			
def SUBCATEGORIES_HinhSu():
		i=0
		for i in range(17):
			addDir('[COLOR yellow]Trang ' + pagestr[i] + '[/COLOR][COLOR red] - Phim Hình Sự [/COLOR]','http://phim3s.net/the-loai/phim-hinh-su/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
		
def SUBCATEGORIES_ChienTrang():	
		i=0
		for i in range(9):		
			addDir('[COLOR blue]Trang ' + pagestr[i] + '[/COLOR][COLOR lime] - Phim Chiến Tranh [/COLOR]','http://phim3s.net/the-loai/phim-chien-tranh/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
 		
def SUBCATEGORIES_ThanThoai():
		i=0
		for i in range(4):
			addDir('[COLOR blue]Trang ' + pagestr[i] + '[/COLOR][COLOR yellow] - Phim Thần Thoại[/COLOR]','http://phim3s.net/the-loai/phim-than-thoai/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
			
def SUBCATEGORIES_VienTuong():
		i=0
		for i in range(19):
			addDir('[COLOR green]Trang ' + pagestr[i] + '[/COLOR][COLOR magenta] - Phim Viễn Tưởng[/COLOR]','http://phim3s.net/the-loai/phim-vien-tuong/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1

def SUBCATEGORIES_CoTrang():
		i=0
		for i in range(14):
			addDir('[COLOR magenta]Trang ' + pagestr[i] + '[/COLOR][COLOR blue] - Phim Cổ Trang [/COLOR]','http://phim3s.net/the-loai/phim-co-trang/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
			
def SUBCATEGORIES_PhieuLuu():
		i=0
		for i in range(22):
			addDir('[COLOR yellow]Trang ' + pagestr[i] + '[/COLOR][COLOR red] - Phim Phiêu Lưu [/COLOR]','http://phim3s.net/the-loai/phim-phieu-luu/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
						
def SUBCATEGORIES_My():
		i=0
		for i in range(90):
			addDir('[COLOR yellow]Trang ' + pagestr[i] + '[/COLOR][COLOR lime] - Phim Mỹ  - Movies & TV Series [/COLOR]','http://phim3s.net/quoc-gia/phim-my/page-' + pagestr[i],16,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/t1.0-1/c33.0.160.160/p160x160/10151272_625399870847304_507077207_n.jpg')
			i+=1
		
def INDEX(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		match=re.compile('<div class="inner"><a href="(.+?)" title="(.+?)"><img src="(.+?)"').findall(link)
		for url,name,thumbnail in match:
				addDir('[COLOR yellow]' + name + '[/COLOR]',('%s%sxem-phim' % (base_url, url)),17,thumbnail)					

		
def VIDEOLINKS(url,name):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		match=re.compile('a data-type="watch" data-episode-id.+?href="(.+?)" title="(.+?)"').findall(link)
		for url,title in match:
				addLink(('%s   -   %s' % ('[COLOR yellow]' + name + '[/COLOR]', '[COLOR lime]' + title + '[/COLOR]')),('%s%svideo.mp4' % (base_url, url)),'')
							                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
                      
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()

elif mode==1:
        SEARCH()
		
elif mode==2:
        print ""
        SUBCATEGORIES_HongKong()

elif mode==3:
        print ""
        SUBCATEGORIES_HANQUOC()	
		
elif mode==4:
        print ""
        SUBCATEGORIES_VietNam()
		
elif mode==5:
        print ""
        SUBCATEGORIES_RAP()
		
elif mode==6:
        print ""
        SUBCATEGORIES_TrungQuoc()
		
elif mode==7:
        print ""
        SUBCATEGORIES_ThaiLan()
		
elif mode==8:
        print ""
        SUBCATEGORIES_HanhDong()

elif mode==9:
        print ""
        SUBCATEGORIES_VoThuat()	
		
elif mode==10:
        print ""
        SUBCATEGORIES_TamLy()
		
elif mode==11:
        print ""
        SUBCATEGORIES_HaiHuoc()
		
elif mode==12:
        print ""
        SUBCATEGORIES_PhieuLuu()
		
elif mode==13:
        print ""
        SUBCATEGORIES_KinhDi()

elif mode==14:
        print ""
        SUBCATEGORIES_HinhSu()

elif mode==15:
        print ""
        SUBCATEGORIES_ChienTrang()	
		
elif mode==18:
        print ""
        SUBCATEGORIES_ThanThoai()
		
elif mode==19:
        print ""
        SUBCATEGORIES_VienTuong()
		
elif mode==20:
        print ""
        SUBCATEGORIES_CoTrang()
		
elif mode==21:
        print ""
        SUBCATEGORIES_My()
	
elif mode==16:
        print ""+url
        INDEX(url)
        
elif mode==17:
        print ""+url
        VIDEOLINKS(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))