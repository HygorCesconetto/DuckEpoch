import { Component, signal } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { BtnSubmitComponent } from '../btn-submit/btn-submit.component';
import { ItemService as ItemService } from '../../services/item.service';

@Component({
  selector: 'app-c-form',
  standalone: true,
  imports: [ReactiveFormsModule, BtnSubmitComponent],
  providers: [ItemService],
  templateUrl: './c-form.component.html',
  styleUrl: './c-form.component.scss'
})

export class CFormComponent {
  cadastroform!: FormGroup;
  loading = signal(false);

  constructor(private service:ItemService){
    this.cadastroform = new FormGroup({
      nome: new FormControl("",[Validators.required]),
      tipo: new FormControl("", [Validators.required]),
      itipo: new FormControl ("",[Validators.required]),
      ataque: new FormControl ("",[Validators.required]),
      defesa: new FormControl ("",[Validators.required]),
      vida: new FormControl ("",[Validators.required]),
      aspeed: new FormControl ("",[Validators.required])
    });
  }

  onSubmit(){
    this.loading.set(true);
    if(this.cadastroform.valid){
      this.service.postItens(this.cadastroform.value.nome,
                            this.cadastroform.value.tipo,
                            this.cadastroform.value.itipo,
                            this.cadastroform.value.ataque,
                            this.cadastroform.value.defesa,
                            this.cadastroform.value.vida,
                            this.cadastroform.value.aspeed).subscribe({
                                  complete: ()=>{
                                    this.cadastroform.reset();
                                    this.loading.set(false);
                                  }
                            })
    }
  }
}