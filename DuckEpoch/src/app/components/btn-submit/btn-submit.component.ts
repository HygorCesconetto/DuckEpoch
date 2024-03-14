import { CommonModule } from '@angular/common';
import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-btn-submit',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './btn-submit.component.html',
  styleUrl: './btn-submit.component.scss'
})
export class BtnSubmitComponent {
    @Input("btn-text") btnText:string ="";
    @Input() disabled:boolean = false;
    @Input() loading:boolean = false;

    @Output ("submit") onSubmit = new EventEmitter();

    submit(){
      this.onSubmit.emit();
    }
}
