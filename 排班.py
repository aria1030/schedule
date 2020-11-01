import pandas as pd

print('影像科专用报排班软件'.center('=' * 50))
print('请按pd_old模式将排班表复制进去')
input()

pb_zd = pd.read_excel('pb_old.xlsx',index_col=0,usecols='A:H')
pb_js = pd.read_excel('pb_old.xlsx',sheet_name='js',index_col=0,usecols='A:H')

pb_zd.replace(['审双','审单','城北','胃肠','白1','白2','白3'],'白班',inplace=True,regex=True)
pb_zd.replace('中晚','中小',inplace=True)
pb_js.replace(['CT2','CT3','结防','重建','DR'],'白班',inplace=True,regex=True)
pb_js.replace('C夜','夜班',inplace=True)
pb_js.replace('上午','上午班',inplace=True)

pb_append = pb_zd.append(pb_js)
pb_append.replace('休假','放射假',inplace=True)
pb_append.index.name ='姓名'
pb_append.rename(index={'李  明':'李明','李  雪':'李雪','王  东':'王东','魏洪渠':'魏红渠',
                             '李  翔':'李翔','王  静':'王静','孟  晨':'孟晨'},inplace=True)
pb_append.replace('下夜','下夜班',inplace=True)


pb_append.to_excel('pb_append.xlsx')

mb = pd.read_excel('mb.xls',index_col=0)
pb_append_read = pd.read_excel('pb_append.xlsx')
pb_final =pd.merge(mb,pb_append_read,on='姓名')
pb_final.loc[32]= ['LLL001','林丽丽','无','外出开会学习','外出开会学习','外出开会学习','外出开会学习','外出开会学习','外出开会学习','外出开会学习']
pb_final.loc[33]= ['LHX002','吕宏新','无','外出开会学习','外出开会学习','外出开会学习','外出开会学习','外出开会学习','外出开会学习','外出开会学习']
pb_final.to_excel('pb_final.xlsx')

print('排班录入已完成，请打开pb_final！')
