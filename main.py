#coding=utf-8
from sys import *
from time import sleep
from os import *
from datetime import datetime

if version[0] in '2':
	exit('\033[93m[!] PROGRAM TIDAK DI DUKUNG PADA PYTHON 2:)')

try:
	from pytube.cli import on_progress
	from pytube import YouTube
except ModuleNotFoundError:
	system('pip3 install pytube')
	try:
		from pytube.cli import on_progress
		from pytube import YouTube
	except ModuleNotFoundError:
		exit('\033[93m[!] GAGAL MENGINSTALL MODUL \033[91m"pytube"')

satu = """\033[94m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     // """
dua = """\033[91m                                 \n@@@@@@@@@@   @@@@@@@      @@@  @@@  \n@@@@@@@@@@@  @@@@@@@@     @@@  @@@  \n@@! @@! @@!  @@!  @@@     @@!  !@@  \n!@! !@! !@!  !@!  @!@     !@!  @!!  \n@!! !!@ @!@  @!@!!@!       !@@!@!   \n!@!   ! !@!  !!@!@!         @!!!    \n!!:     !!:  !!: :!!       !: :!!   \n:!:     :!:  :!:  !:!     :!:  !:!  \n:::     ::   ::   :::      ::  :::  \n:      :     :   : :      :   ::                                  """

def tabel_waktu(a):
	print (a)
	
	sekarang = datetime.now()

	hari = sekarang.day
	
	bulan = sekarang.month
	
	tahun = sekarang.year
	
	jam = sekarang.hour
	
	menit = sekarang.minute
	
	detik = sekarang.second
	
	tahun = sekarang.year
	
	print ("\033[91m╔═════════════════════════════════════╗\n║\033[91m[\033[93m•\033[91m] \033[92mAuthor : \033[93mMR-X JUNIOR             ║\n║\033[91m[\033[93m•\033[91m] \033[92mGitHub : \033[94mgithub.com/MR-X-Junior  ║\n║\033[91m[\033[93m•\033[91m] \033[92mWA.    : \033[95m+6285754629509          ║\n║\033[91m[\033[93m•\033[91m] \033[92mUPDATE : \033[96m9-1-2021 05:01       ║")
	print ("\033[92m║\033[91m[\033[93m•\033[91m] \033[92mDATE   : \033[93m{}-\033[94m{}-\033[95m{} \033[96m{}:\033[96m{}:\033[96m{}     |\n|\033[91m[\033[93m•\033[91m] \033[92mOS     : \033[96m\033[91m{}      \033[95m             |\n|\033[91m[\033[93m•\033[91m] \033[92mVERSI  : \033[96m\033[92m1.0       \033[95m              |\n\033[97m╚═════════════════════════════════════╝".format(hari, bulan, tahun, jam, menit, detik, platform))
	
def main():
	system('clear')
	try:
		tabel_waktu(satu) ; print('\033[92mDOWNLOAD VIDEO YOUTUBE') ; print (20* '\033[96m=')
		link = input('\033[92m[?] LINK VIDEO : \033[93m')
		if link == "":
			main()
		else:
			print ('\033[93m[!] MOHON TUNGGU') ; sleep(1)
			url = YouTube (link,on_progress_callback=on_progress)
			while True:
				system('clear') ; tabel_waktu(dua) ; print ('\033[93mRINCIAN VIDEO') ; print (20* '\033[96m=')
				print (f'\033[92m[✓] LINK  : \033[93m"{link}"')
				print (f'\033[92m[✓] JUDUL : \033[94m"{url.title}"')
				print(f'\033[92m[✓] ID    : \033[95m"{url.video_id}"')
				print (f'\033[92m[✓] VIEW  : \033[96m"{url.views}"')
				print (f'\033[92m[✓] RATING : \033[97m"{url.rating}"')
				print (f'\033[92m[✓] BATASAN USIA: \033[91m"{url.age_restricted}"')
				print (f'\033[92m[✓] EMBED URL : \033[93m"{url.embed_url}"')
				a = input('\033[93m[?] DOWNLOAD VIDEO \033[94m[\033[92mY\033[93m/\033[91mN\033[94m] \033[95m').upper()
				if a == "":
					system('clear')
				elif a == "Y" or a == "YES":
					print ('\033[95m[!] MENDOWNLOAD VIDEO')
					url.streams\
						.filter(file_extension='mp4')\
						.get_highest_resolution()\
						.download(path.curdir+ "/video")
					print ('\n\033[92m[✓] DOWNLOAD SELESAI')
					i = input ('\033[92m[?] BACK [\033[96mY\033[92m/\033[93mN] ').upper()
					if i == "Y" or a== "YES":
						main()
					elif i == "N" or a == "NO":
						break
					else:
						print ('\033[93m[!] PILIHAN TIDAK TERSEDIA') ; break
					
				elif a == "N" or a == "NO":
					main()
				else:
					print (f'\033[93m[!] KATA KUNCI DARI \033[91m"{a}" \033[93mTIDAK DI TEMUKAN') ; sleep(2) ; system('clear')
	except ModuleNotFoundError:
		system('pip3 install pytube')
	except PermissionError:
		exit('\033[91m[!] GAGAL MENGAKSES PENYIMPANAN')
	except ConnectionResetError:
		exit('\033[93m[!] SAMBUNGAN KE SERVER TERPUTUS')
	except KeyboardInterrupt:
		exit()
	except TimeoutError:
		exit('\033[93m[!] KONEKSI LAMBAT\n[!] GAGAL TERHUBUNG KE SERVER')
	except Exception as salah:
		exit('\033[93m[!] TERJADI KESALAHAN\n\033[93m[!] INFO ERROR :\033[95m{}'.format(salah))
		
def main2(link):
	system('clear')
	try:
		tabel_waktu(satu) ; print('\033[92mDOWNLOAD VIDEO YOUTUBE') ; print (20* '\033[96m=')
		print (f'\033[92m[?] LINK VIDEO : \033[93m{argv[-1]}')
		print ('\033[93m[!] MOHON TUNGGU') ; sleep(1)
		url = YouTube (link,on_progress_callback=on_progress)
		while True:
			system('clear') ; tabel_waktu(dua) ; print ('\033[93mRINCIAN VIDEO') ; print (20* '\033[96m=')
			print (f'\033[92m[✓] LINK  : \033[93m"{link}"')
			print (f'\033[92m[✓] JUDUL : \033[94m"{url.title}"')
			print(f'\033[92m[✓] ID    : \033[95m"{url.video_id}"')
			print (f'\033[92m[✓] VIEW  : \033[96m"{url.views}"')
			print (f'\033[92m[✓] RATING : \033[97m"{url.rating}"')
			print (f'\033[92m[✓] BATASAN USIA: \033[91m"{url.age_restricted}"')
			print (f'\033[92m[✓] EMBED URL : \033[93m"{url.embed_url}"')
			a = input('\033[93m[?] DOWNLOAD VIDEO \033[94m[\033[92mY\033[93m/\033[91mN\033[94m] \033[95m').upper()
			if a == "":
				system('clear')
			elif a == "Y" or a == "YES":
				print ('\033[95m[!] MENDOWNLOAD VIDEO')
				url.streams\
					.filter(file_extension='mp4')\
					.get_highest_resolution()\
					.download(path.curdir+ "/video")
				exit ('\n\033[92m[✓] DOWNLOAD SELESAI')
			elif a == "N" or a == "NO":
					exit()
			else:
				exit()
	except ModuleNotFoundError:
		system('pip3 install pytube')
	except PermissionError:
		exit('\033[91m[!] GAGAL MENGAKSES PENYIMPANAN')
	except ConnectionResetError:
		exit('\033[93m[!] SAMBUNGAN KE SERVER TERPUTUS')
	except KeyboardInterrupt:
		exit()
	except TimeoutError:
		exit('\033[93m[!] KONEKSI LAMBAT\n[!] GAGAL TERHUBUNG KE SERVER')
	except Exception as salah:
		exit('\033[93m[!] TERJADI KESALAHAN\n\033[93m[!] INFO ERROR :\033[95m{}'.format(salah))
		
		
if __name__=="__main__":
	if len(argv) == 2:
		main2(argv[1])
	elif len(argv) > 2:
		system('clear')
		print ('\033[95m')
		raise TypeError('\033[93mCommand Tidak Di Kenali')
	else:
		main()