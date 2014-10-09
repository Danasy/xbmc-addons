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

import urllib,urllib2,re,xbmcplugin,xbmcgui
pagestr    = map(str, range(1,50))

def home():
        addDir('[COLOR lime][B]Tìm Nhạc  >>>>  Music Search[/B][/COLOR]','http://nhacso.net/',1,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')		
        addDir('[COLOR lime]Video Clips - Thể Loại[/COLOR]','http://nhacso.net/the-loai-video/nhac-tre-1/trang-1.html',2,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
        addDir('[COLOR lime]Video Clips - Nghệ Sĩ Việt Nam[/COLOR]','http://nhacso.net/video-cua-nghe-si/cam-ly-17-1-1.html',2,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
        addDir('[COLOR lime]Video Clips - Nghệ Sĩ Quốc Tế[/COLOR]','http://nhacso.net/video-cua-nghe-si/2ne1-3760-1-1.html',2,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')


def dirs():
		if 'the-loai' in url:
				addDir('[COLOR lime]Nhạc Trẻ[/COLOR]','http://nhacso.net/the-loai-video/nhac-tre-1/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Trữ Tình[/COLOR]','http://nhacso.net/the-loai-video/nhac-tru-tinh-2/trang-1.html/',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Quê Hương[/COLOR]','http://nhacso.net/the-loai-video/nhac-que-huong-11/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc dân Tộc[/COLOR]','http://nhacso.net/the-loai-video/nhac-dan-toc-6/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Trịnh[/COLOR]','http://nhacso.net/the-loai-video/nhac-trinh-4/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Tiền Chiến[/COLOR]','http://nhacso.net/the-loai-video/nhac-tien-chien-5/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Thiếu Nhi[/COLOR]','http://nhacso.net/the-loai-video/nhac-thieu-nhi-7/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Rock Việt[/COLOR]','http://nhacso.net/the-loai-video/rock-viet-9/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Rap Việt - HipHop[/COLOR]','http://nhacso.net/the-loai-video/rap-viet-hiphop-14/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Âu Mỹ[/COLOR]','http://nhacso.net/the-loai-video/nhac-au-my-21/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Hàn[/COLOR]','http://nhacso.net/the-loai-video/nhac-han-16/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Hoa[/COLOR]','http://nhacso.net/the-loai-video/nhac-hoa-15/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Nhật[/COLOR]','http://nhacso.net/the-loai-video/nhac-nhat-32/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Pháp[/COLOR]','http://nhacso.net/the-loai-video/nhac-phap-17/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhạc Các Nước Khác[/COLOR]','http://nhacso.net/the-loai-video/nhac-cac-nuoc-khac-18/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Nhân Tố Bí Ẩn[/COLOR]','http://nhacso.net/the-loai-video/nhan-to-bi-an-82/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Truyền Hình HomeTV[/COLOR]','http://nhacso.net/the-loai-video/truyen-hinh-hometv-81/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Giọng Hát Việt Nhí[/COLOR]','http://nhacso.net/the-loai-video/giong-hat-viet-nhi-68/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Fanmade / Radio[/COLOR]','http://nhacso.net/the-loai-video/fanmade-radio-66/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Shining Show[/COLOR]','http://nhacso.net/the-loai-video/shining-show-63/trang-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
		if 'cam-ly' in url:
				addDir('[COLOR lime]Cẩm Ly[/COLOR]','http://nhacso.net/video-cua-nghe-si/cam-ly-17-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Dương Ngọc Thái[/COLOR]','http://nhacso.net/video-cua-nghe-si/duong-ngoc-thai-789-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Đàm Vĩnh Hưng[/COLOR]','http://nhacso.net/video-cua-nghe-si/dam-vinh-hung-47-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Đan Trường[/COLOR]','http://nhacso.net/video-cua-nghe-si/dan-truong-55-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Hồ Ngọc Hà[/COLOR]','http://nhacso.net/video-cua-nghe-si/ho-ngoc-ha-33-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Khắc Việt[/COLOR]','http://nhacso.net/video-cua-nghe-si/khac-viet-4481-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Lam Trường[/COLOR]','http://nhacso.net/video-cua-nghe-si/lam-truong-4-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Lệ Quyên[/COLOR]','http://nhacso.net/video-cua-nghe-si/le-quyen-3-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Ngô Kiến Huy[/COLOR]','http://nhacso.net/video-cua-nghe-si/ngo-kien-huy-2228-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Noo Phước Thịnh[/COLOR]','http://nhacso.net/video-cua-nghe-si/noo-phuoc-thinh-2430-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Phương Thanh[/COLOR]','http://nhacso.net/video-cua-nghe-si/phuong-thanh-110-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Quang Dũng[/COLOR]','http://nhacso.net/video-cua-nghe-si/quang-dung-79-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]The Men[/COLOR]','http://nhacso.net/video-cua-nghe-si/the-men-2407-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Thuỷ Tiên[/COLOR]','http://nhacso.net/video-cua-nghe-si/thuy-tien-2429-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Uyên Linh[/COLOR]','http://nhacso.net/video-cua-nghe-si/uyen-linh-4525-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Văn Mai Hương[/COLOR]','http://nhacso.net/video-cua-nghe-si/van-mai-huong-3159-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Vmusic[/COLOR]','http://nhacso.net/video-cua-nghe-si/vmusic-4540-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
		if '2ne1-3760' in url:
				addDir('[COLOR lime]2NE1[/COLOR]','http://nhacso.net/video-cua-nghe-si/2ne1-3760-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]2PM[/COLOR]','http://nhacso.net/video-cua-nghe-si/2pm-3762-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Adele[/COLOR]','http://nhacso.net/video-cua-nghe-si/adele-5903-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Avril Lavigne[/COLOR]','http://nhacso.net/video-cua-nghe-si/avril-lavigne-2496-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Beyonce[/COLOR]','http://nhacso.net/video-cua-nghe-si/beyonce-2530-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Big Bang[/COLOR]','http://nhacso.net/video-cua-nghe-si/big-bang-2536-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Britney Spears[/COLOR]','http://nhacso.net/video-cua-nghe-si/britney-spears-2568-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Girls Generation[/COLOR]','http://nhacso.net/video-cua-nghe-si/snsd-girls-generation-2802-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Jay Chou - Châu[/COLOR]','http://nhacso.net/video-cua-nghe-si/jay-chou-chau-kiet-luan-2926-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Justin Bieber[/COLOR]','http://nhacso.net/video-cua-nghe-si/justin-bieber-2976-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Kelly Clarkson[/COLOR]','http://nhacso.net/video-cua-nghe-si/kelly-clarkson-3011-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Lady Gaga[/COLOR]','http://nhacso.net/video-cua-nghe-si/lady-gaga-3074-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Rihanna[/COLOR]','http://nhacso.net/video-cua-nghe-si/rihanna-3375-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]S.H.E[/COLOR]','http://nhacso.net/video-cua-nghe-si/s-h-e-3405-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]Super Junior[/COLOR]','http://nhacso.net/video-cua-nghe-si/super-junior-3514-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
				addDir('[COLOR lime]TVXQ (DBDK)[/COLOR]','http://nhacso.net/video-cua-nghe-si/dbsk-tvxq-5218-1-1.html',3,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
		
def pagelist():
		if 'nhac-tre' in url:
				i=0
				for i in range(42):
						addDir('[COLOR lime]Nhạc Trẻ Trang[/COLOR]' + pagestr[i] + '','http://nhacso.net/the-loai-video/nhac-tre-1/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1
		if 'nhac-tru-tinh' in url:
				i=0
				for i in range(42):		
						addDir('[COLOR lime]Nhạc Trữ Tình Trang[/COLOR] ' + pagestr[i] + '','http://nhacso.net/the-loai-video/nhac-tru-tinh-2/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'nhac-que-huong' in url:
				i=0
				for i in range(18):
						addDir('[COLOR lime]Nhạc Quê Hương Trang[/COLOR] ' + pagestr[i] + '','http://nhacso.net/the-loai-video/nhac-que-huong-11/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'nhac-dan-toc' in url:
				i=0
				for i in range(37):
						addDir('[COLOR lime]Nhạc dân Tộc Trang[/COLOR] ' + pagestr[i] + '','http://nhacso.net/the-loai-video/nhac-dan-toc-6/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1			
		if 'nhac-trinh' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Nhạc Trịnh Trang[/COLOR] ' + pagestr[i] + '','http://nhacso.net/the-loai-video/nhac-trinh-4/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'nhac-tien-chien' in url: 	
				i=0
				for i in range(4):		
						addDir('[COLOR lime]Nhạc Tiền Chiến Trang[/COLOR] ' + pagestr[i] + '','http://nhacso.net/the-loai-video/nhac-tien-chien-5/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'nhac-thieu-nhi' in url:
				i=0
				for i in range(10):
						addDir('[COLOR lime]Nhạc Thiếu Nhi Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/nhac-thieu-nhi-7/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1						
		if 'rock-viet' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Rock Việt Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/rock-viet-9/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'rap-viet-hiphop' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR lime]Rap Việt - HipHop Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/rap-viet-hiphop-14/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'nhac-au-my' in url:
				i=0
				for i in range(42):
						addDir('[COLOR lime]Nhạc Âu Mỹ Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/nhac-au-my-21/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'nhac-han' in url:
				i=0
				for i in range(42):
						addDir('[COLOR lime]Nhạc Hàn Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/nhac-han-16/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1			
		if 'nhac-hoa' in url:
				i=0
				for i in range(42):
						addDir('[COLOR lime]Nhạc Hoa Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/nhac-hoa-15/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'nhac-nhat' in url: 	
				i=0
				for i in range(42):		
						addDir('[COLOR lime]Nhạc Nhật Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/nhac-nhat-32/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'nhac-phap' in url:
				i=0
				for i in range(1):
						addDir('[COLOR lime]Nhạc Pháp Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/nhac-phap-17/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1						
		if 'nhac-cac-nuoc-khac' in url:
				i=0
				for i in range(18):
						addDir('[COLOR lime]Nhạc Các Nước Khác Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/nhac-cac-nuoc-khac-18/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'nhan-to-bi-an' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR lime]Nhân Tố Bí Ẩn Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/nhan-to-bi-an-82/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'truyen-hinh-hometv' in url:
				i=0
				for i in range(1):
						addDir('[COLOR lime]Truyền Hình HomeTV Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/truyen-hinh-hometv-81/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'giong-hat-viet-nhi' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Giọng Hát Việt Nhí Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/giong-hat-viet-nhi-68/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1			
		if 'fanmade-radio' in url:
				i=0
				for i in range(3):
						addDir('[COLOR lime]Fanmade / Radio Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/fanmade-radio-66/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'shining-show' in url: 	
				i=0
				for i in range(4):		
						addDir('[COLOR lime]Shining Show Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/the-loai-video/shining-show-63/trang-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1						
		if 'cam-ly' in url:
				i=0
				for i in range(18):
						addDir('[COLOR lime]Cẩm Ly Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/cam-ly-17-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'duong-ngoc-thai' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR lime]Dương Ngọc Thái Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/duong-ngoc-thai-789-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'dam-vinh-hung' in url:
				i=0
				for i in range(13):
						addDir('[COLOR lime]Đàm Vĩnh Hưng Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/dam-vinh-hung-47-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'dan-truong' in url:
				i=0
				for i in range(23):
						addDir('[COLOR lime]Đan Trường Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/dan-truong-55-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1			
		if 'ho-ngoc-ha' in url:
				i=0
				for i in range(9):
						addDir('[COLOR lime]Hồ Ngọc Hà Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/ho-ngoc-ha-33-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'khac-viet' in url: 	
				i=0
				for i in range(3):		
						addDir('[COLOR lime]Khắc Việt Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/khac-viet-4481-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'lam-truong' in url:
				i=0
				for i in range(6):
						addDir('[COLOR lime]Lam Trường Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/lam-truong-4-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1						
		if 'le-quyen' in url:
				i=0
				for i in range(6):
						addDir('[COLOR lime]Lệ Quyên Trang' + pagestr[i] + '','http://nhacso.net/video-cua-nghe-si/le-quyen-3-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'ngo-kien-huy' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR lime]Ngô Kiến Huy Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/ngo-kien-huy-2228-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'noo-phuoc-thinh' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Noo Phước Thịnh Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/noo-phuoc-thinh-2430-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'phuong-thanh' in url:
				i=0
				for i in range(7):
						addDir('[COLOR lime]Phương Thanh Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/phuong-thanh-110-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1			
		if 'quang-dung' in url:
				i=0
				for i in range(3):
						addDir('[COLOR lime]Quang Dũng Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/quang-dung-79-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'the-men' in url: 	
				i=0
				for i in range(4):		
						addDir('[COLOR lime]The Men Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/the-men-2407-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'thuy-tien' in url:
				i=0
				for i in range(3):
						addDir('[COLOR lime]Thuỷ Tiên Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/thuy-tien-2429-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1						
		if 'uyen-linh' in url:
				i=0
				for i in range(2):
						addDir('[COLOR lime]Uyên Linh Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/uyen-linh-4525-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'van-mai-huong' in url:
				i=0
				for i in range(4):		
						addDir('[COLOR lime]Văn Mai Hương Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/van-mai-huong-3159-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'vmusic' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Vmusic Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/vmusic-4540-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if '2ne1' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]2NE1 Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/2ne1-3760-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1			
		if '2pm' in url:
				i=0
				for i in range(6):
						addDir('[COLOR lime]2PM Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/2pm-3762-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'adele' in url: 	
				i=0
				for i in range(2):		
						addDir('[COLOR lime]Adele Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/adele-5903-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1
		if 'avril-lavigne' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Avril Lavigne Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/avril-lavigne-2496-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'beyonce' in url:
				i=0
				for i in range(8):
						addDir('[COLOR lime]Beyonce Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/beyonce-2530-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'big-bang' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Big Bang Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/big-bang-2536-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1			
		if 'britney-spears' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Britney Spears Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/britney-spears-2568-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'snsd-girls-generation' in url: 	
				i=0
				for i in range(18):		
						addDir('[COLOR lime]Girls Generation Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/snsd-girls-generation-2802-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'jay-chou-chau-kiet-luan' in url:
				i=0
				for i in range(13):
						addDir('[COLOR lime]Jay Chou - Châu Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/jay-chou-chau-kiet-luan-2926-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1						
		if 'justin-bieber' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Justin Bieber Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/justin-bieber-2976-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'kelly-clarkson' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR lime]Kelly Clarkson Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/kelly-clarkson-3011-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'lady-gaga' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]Lady Gaga Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/lady-gaga-3074-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'rihanna' in url:
				i=0
				for i in range(6):
						addDir('[COLOR lime]Rihanna Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/rihanna-3375-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1			
		if 's-h-e' in url:
				i=0
				for i in range(12):
						addDir('[COLOR lime]S.H.E Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/s-h-e-3405-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1		
		if 'super-junior' in url: 	
				i=0
				for i in range(4):		
						addDir('[COLOR lime]Super Junior Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/super-junior-3514-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1 		
		if 'dbsk-tvxq' in url:
				i=0
				for i in range(6):
						addDir('[COLOR lime]TVXQ (DBDK) Trang' + pagestr[i] + [/COLOR]'','http://nhacso.net/video-cua-nghe-si/dbsk-tvxq-5218-1-' + pagestr[i] + '.html',4,'http://st.nhacso.net/c/v3/images/graphics/Nhacso_logo.jpg')
						i+=1
								
def index(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		if 'the-loai-video' in url:
				match=re.compile('<a href="(.*?)" title="(.+?)".+?\s.*?src="(.*?)" width').findall(link)
				for url,name,thumbnail in match:
						addDir('' + name + '',url,5,thumbnail)						
		else:
				match=re.compile('<a class="png_img playlist" href="(.+?)" title="(.+?)".+?\s.*?src="(.+?)" onerror').findall(link)
				for url,name,thumbnail in match:
						addDir('' + name + '',url,5,thumbnail)
					
def videolinks(url,name):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		match=re.compile('src="(.+?)" data-setup').findall(link)		
		for url in match:
				addLink(name,url,'')
	
def search():
    try:
        keyb = xbmc.Keyboard('', 'Enter search text')
        keyb.doModal()
        if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText())
        url = 'http://nhacso.net/?KeyName='+searchText
        index(url)
    except: pass
	
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
        home()

elif mode==1:
        search()	

elif mode==2:
        print ""
        dirs()	
		
elif mode==3:
        print ""
        pagelist()		
		
elif mode==4:
        print ""+url
        index(url)
		
elif mode==5:
        print ""+url
        videolinks(url,name)
			
xbmcplugin.endOfDirectory(int(sys.argv[1]))