import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CadastroItensComponent } from './cadastro-itens.component';

describe('CadastroItensComponent', () => {
  let component: CadastroItensComponent;
  let fixture: ComponentFixture<CadastroItensComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CadastroItensComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CadastroItensComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
