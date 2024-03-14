import { Routes } from '@angular/router';
import { CadastroItensComponent } from './pages/cadastro-itens/cadastro-itens.component';
import { ConsultaItensComponent } from './pages/consulta-itens/consulta-itens.component';

export const routes: Routes = [
    {
        path: "",
        component: CadastroItensComponent
    },
    {
        path: "itens/cadastro",
        component: CadastroItensComponent
    },
    {
        path: "itens/consultar",
        component: ConsultaItensComponent
    },
    {
        path: "itens/deletar",
        component: CadastroItensComponent
    },
    {
        path: "itens/atualizar",
        component: CadastroItensComponent
    }
];
