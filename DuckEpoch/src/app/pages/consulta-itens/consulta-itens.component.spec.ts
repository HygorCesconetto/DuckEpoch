import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsultaItensComponent } from './consulta-itens.component';

describe('ConsultaItensComponent', () => {
  let component: ConsultaItensComponent;
  let fixture: ComponentFixture<ConsultaItensComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ConsultaItensComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ConsultaItensComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
