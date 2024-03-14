import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeletaItensComponent } from './deleta-itens.component';

describe('DeletaItensComponent', () => {
  let component: DeletaItensComponent;
  let fixture: ComponentFixture<DeletaItensComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DeletaItensComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DeletaItensComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
