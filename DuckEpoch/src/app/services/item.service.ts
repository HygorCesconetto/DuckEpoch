import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';



interface CadItemResponse {
  message: string
}

@Injectable({
  providedIn: 'root'
})
export class ItemService {
  private endpoint ="http://127.0.0.1:5000/";
  data:any =[];

  constructor(private http:HttpClient) {}

  postItens(nome:string, tipo:string, itipo:string, ataque:number, defesa:number, vida:number, aspeed:number): Observable<CadItemResponse>{
    ataque = Math.trunc(ataque);
    defesa = Math.trunc(defesa);
    vida = Math.trunc(vida);

    var data: any
    var forurl:string

    if(itipo === "weapon"){
      data = {"name":nome, "type":tipo, "atk":ataque, "def":defesa, "atks":aspeed};
      forurl = "weapon"

    } else if(itipo === "armour"){
      data = {"name":nome, "type":tipo, "atk":ataque, "def":defesa, "hp":vida};
      forurl = "armour"

    } else {
      data = {"name":nome, "type":tipo, "atk":ataque, "def":defesa, "hp":vida};
      forurl = "trinket"
    }

    return this.http.post <CadItemResponse> (this.endpoint+forurl, data);
  }

fetchData(titem:string, tipo:string, prop:string){
  var endurl:string
  if (titem=== "weapon"){
      endurl = "weapon"
    if(tipo ==="all"){
      this.http.get(this.endpoint+endurl).subscribe(
        (data)=>{
          console.log(data);
          this.data = data;
        }
      )
    }
  }
}

}
