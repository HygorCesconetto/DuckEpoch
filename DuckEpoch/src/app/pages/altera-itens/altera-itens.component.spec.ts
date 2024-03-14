import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlteraItensComponent } from './altera-itens.component';

describe('AlteraItensComponent', () => {
  let component: AlteraItensComponent;
  let fixture: ComponentFixture<AlteraItensComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AlteraItensComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AlteraItensComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
