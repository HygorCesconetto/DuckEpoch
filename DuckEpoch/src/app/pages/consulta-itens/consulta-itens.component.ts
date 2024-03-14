import { Component, signal } from '@angular/core';
import { BtnSubmitComponent } from '../../components/btn-submit/btn-submit.component';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ItemService } from '../../services/item.service';

@Component({
  selector: 'app-consulta-itens',
  standalone: true,
  imports: [BtnSubmitComponent, ReactiveFormsModule],
  providers: [ItemService],
  templateUrl: './consulta-itens.component.html',
  styleUrl: './consulta-itens.component.scss'
})
export class ConsultaItensComponent {
loading = signal(false);
form_consulta!: FormGroup;

constructor(private service: ItemService){
  this.form_consulta = new FormGroup({
    titem: new FormControl("",[Validators.required]),
    tipo: new FormControl("",[Validators.required]),
    prop: new FormControl("",[Validators.required])
  })
};

  onSubmit(){
    this.loading.set(true)
    if(this.form_consulta.valid){
      this.service.fetchData(this.form_consulta.value.titem, this.form_consulta.value.tipo, this.form_consulta.value.prop)
    }
    this.loading.set(false)                  
  }
}