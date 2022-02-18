from django.shortcuts import render, redirect
from .templates import*

# Create your views here.
def keitai(request):
    return render(request,'keitai.html')

def result(request):
    if request.method == "POST":
        if "btn" in request.POST:
                
            docomo=0
            softbank=0
            au=0
            rakuten=0
            plan_d="5Gギガライト"
            plan_s="ミニフィットプラン＋"
            plan_a="ピタットプラン5G"
            plan_r="Rakuten UN-LIMIT VI"
            docomo_f=0
            softbank_f=0
            au_f=0
            docomo_c=0
            softbank_c=0
            au_c=0
            docomo_m=0
            softbank_m=0
            au_m=0
            rakuten_m=0
            docomo_y=0
            softbank_y=0
            au_y=0
            rakuten_y=0

            data_str=request.POST.get("data")
            family_str=request.POST.get("family")
            call_str=request.POST.get("call")
            data=int(data_str)
            family=int(family_str)
            call=int(call_str)
            
            if data==1:
                docomo=3465
                softbank=3278
                au=3465
                rakuten=0
            elif data==2:
                docomo=4565
                au=5115
                rakuten=1078
            elif data==3:
                docomo=4565
                au=5115
                rakuten=1078
            elif data==4:
                docomo=5665
                au=5115
            elif data==5:
                docomo=5665
                au=5115
            elif data==7:
                docomo=6765
                au=5115
            elif data==8:
                docomo=7315
                plan_d="5Gギガホプレミア"
                au=7238
                plan_a="使い放題MAX 5G/4G"
                
            if data>=2:
                softbank=7238
                plan_s="メリハリ無制限"

            if data>=4:
                rakuten=2178
        
            if family==3:
                docomo_f=-1100
                au_f=-1100
                if data>=2:
                    softbank_f=-1210
            elif family==2:
                docomo_f=-550
                au_f=-550
                if data>=2:
                    softbank_f=-660
            """5分通話無料"""
            if call==1:
                docomo_c=770
                softbank_c=880
                au_c=770
            """かけ放題"""
            if call==2:
                docomo_c=1870
                softbank_c=1980
                au_c=1870

            docomo_m=docomo+docomo_f+docomo_c
            softbank_m=softbank+softbank_f+softbank_c
            au_m=au+au_f+au_c
            rakuten_m=rakuten
            docomo_y=docomo_m*12
            softbank_y=softbank_m*12
            au_y=au_m*12
            rakuten_y=rakuten_m*12



            return render(request,'result.html',{"d":docomo,"s":softbank,"a":au,"r":rakuten,
            "p_d":plan_d,"p_s":plan_s,"p_a":plan_a,"p_r":plan_r,
            "d_f":docomo_f,"s_f":softbank_f,"a_f":au_f,
            "d_c":docomo_c,"s_c":softbank_c,"a_c":au_c,
            "d_m":docomo_m,"s_m":softbank_m,"a_m":au_m,"r_m":rakuten_m,
            "d_y":docomo_y,"s_y":softbank_y,"a_y":au_y,"r_y":rakuten_y})
    else:
        return redirect("keitai")