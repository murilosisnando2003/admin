# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'acabamento_placa_circ_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acao_etapa_proced'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acervo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acervo_area'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acervo_assunto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acervo_autor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acervo_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acervo_exemp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acervo_idioma'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acervo_marc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acervo_valid'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aces_atend'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aces_item_aux_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aces_item_aux_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aces_item_aux_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aces_item_aux_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aces_item_solic_amostra'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aces_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acom_item_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acom_item_ped_tur_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acom_item_ped_tur_promocao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acomp_campanha'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acomp_contrato_fisico'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acond_item_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acond_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_tur_cond_rec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_tur_excec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_tur_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda_cond_pag'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda_desp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda_excec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda_nf_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda_nf_fat_dev'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda_parc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda_parc_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda_parc_nf_dev'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'acordo_venda_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ad_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'adiantamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'adiantamento_ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'adiantamento_local'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'adiantamento_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'adiantamento_ord_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'adiantamento_ret'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'adiantamento_ret_centro_ctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'adiantamento_saida'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aerop_cidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aeroporto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ag_bancaria'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agencia_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio_classif'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio_conexao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio_qtd'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio_qtd_item'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio_regime'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio_rota'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_bloqueio_unid_med'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_data_frete_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_data_pacote_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_part_ped_evento_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_ped_evento_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_tarifario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agenda_web'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'agrupamento_iss'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ajuste_apuracao_imp_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ajuste_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ajuste_dimensao_ctrl_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ajuste_item_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ajuste_mov_estq_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ajuste_relatorio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ajuste_relatorio1'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alarme'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alarme_grp_usu'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alarme_metadt'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alarme_parm'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alarme_trf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alarme_visual'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aliq_item_apur_imposto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aliq_item_mapa_resumo_ecf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'allotment'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aloj_ofer_brasil'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alt_comp_item_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alt_questao_questionario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alter_banco_paf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'alternativa'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aluno'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aluno_aula_falta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aluno_disc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aluno_disc_aval'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aluno_disc_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aluno_disc_periodo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aluno_doc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aluno_modulo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'am_parametros_mix'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'anotacao_menu_sistema'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aop'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aplic_aval'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aplic_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aplicacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aplicacao_compl_aplic'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aplicacao_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aplicacao_questionario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aplicar_ent_item_contr_sobre'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aplicar_item_contrato_sobre'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'apolo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'apont_ord_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'apont_ord_produc_pc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'apont_ord_produc_pc_variac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'apont_ordem_proposta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aprov_comp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aprov_comp_finalidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aprov_comp_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aptidao_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'apur_imp_guia_rec_imp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'apur_imp_lucro_presumido'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'apuracao_imposto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'area_formacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'area_resp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'area_resp_funcionario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'area_resp_vinc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'arq_estq_cat44'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'arq_rem'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'arq_rem_reg'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'arq_rem_reg_it'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'array_ajuste_valor_unitario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'assunto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atend_ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atend_item_ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atend_item_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atend_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atendimento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_cargo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_cargo_indir'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_cctrl_aux'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_classe_rec_desp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_direc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_economica'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_oper'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ativ_turno'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atividade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atividade_grupo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atrib_aula_disc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atrib_carta_cor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'atualizar_qtd_desm_mov_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aula'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aula_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aula_recurso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'autenticacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'autor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'autoriz_etapa_proced'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aval_conc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'avaliacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'avaliador_aplic_quest'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aviso_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'aviso_tipo_etapa'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bairro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'baixa_comis'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'banco'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bapscript'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'beneficio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_analisevendas'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_analise_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_analise_estq_retro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_analisebacklog'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_budget'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_compras'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_curva_abc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_curva_resumido'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_dead_inventory'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_edi_managed_lines'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_excess_inventory'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_excess_inventory_op'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_faturamento_review'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_indicesatisfacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_inventory_turns'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_inventory_turns_ra'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_metasaop_faturamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_metasaop_vendas'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_orders_review'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_prazomedio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_primary_adoption'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_primary_readiness'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_propostaelaborada'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_pvliberado'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_supplier_payable_days'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_supplier_return_rate'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_supplier_shipped'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_supplier_toct'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_titulosematraso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_table_vendas_painel'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_tb_dead_inventory_op'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_tb_inventory_availability'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bi_view_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bibliog_plano_ensino'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bico'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bilh_conj_pas_item_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bkp_rateiopedcomp_semclrd'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bloqueio_documento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'bu'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'busca_person'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'busca_person_chave'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'busca_person_filtro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'busca_person_filtro_campo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cad_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'caixa_loja'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'caixa_loja_intervencao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'calc_icms_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'camp_canc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'camp_emailmark'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'camp_faxmark'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'camp_tlmark'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'campanha'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'campanha_promocional'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'campanha_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'campo_ent_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'campo_prod_oper'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cand_ofer_aloj'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cand_ofer_estag'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'candidato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'carac_imov_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'caracter_especific_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'caracter_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cargo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cart_cobranca'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cart_cred_band'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cart_cred_cobrand'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cart_cred_operacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cart_cred_parcela'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cart_cred_tipo_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'carta_cor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'carta_cor_eletronica_trans'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'carta_cor_trans_arq_xml_det'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_amex_ajuste'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_amex_cabecalho'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_amex_cancel_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_amex_pricing'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_amex_recibo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_amex_reg_pagamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_amex_resumo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_amex_trailler'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_concilia_doc_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_concilia_parc_amex'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_concilia_parc_pag'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_concilia_parc_redecard'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_cred_aluguel_pos'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_deb_redecard_cab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_deb_redecard_des'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_deb_redecard_detalhe'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_deb_redecard_resumo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_deb_redecard_total'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_deb_redecard_trans'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_rede_cancel_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_ajuste_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_ajuste_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_ajuste_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_ajuste_net_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_antecip_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_cab_matriz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_cabecalho'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_cabecalho_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_cred_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_deb_pl_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_desagparc_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_detalhe'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_parcelas'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_request'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_resumo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_tot_cred_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_tot_mat_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_totalizador'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_trailler'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_redecard_trailler_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_visa_cabecalho'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_visa_cancel_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_visa_deb_ro_ant'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_visa_det_ant'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_visa_detalhe'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_visa_inf_ro_ant'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cartao_visa_resumo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cat26_mem_calc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cat26_mem_calc_tot'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cat26_reg0150'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cat_grpmprod_vend_meta_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'categ_ent_componente_pv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'categ_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'categ_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'categ_voo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'categoria'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'categoria_foto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'categoria_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'causa_defeito'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cc_eletronica_trans_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cctrl_depara'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cctrl_depara_bkp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cctrl_etapa_lote_criacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cctrl_item_contab_rel'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cctrl_item_ped_venda_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cctrl_tipo_req'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'centro_ctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'centro_ctrl_conta_contab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'centro_ctrl_mix'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'centro_ctrl_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cep'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cert_reg_cad'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cest'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cest_ncm'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'chapa_pap'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'chk_rec_item_mov_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cia_aerea'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cia_aerea_base_tarif'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cia_aerea_gateway'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cia_aerea_pais_dest'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cia_aerea_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ciap'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cid_meta_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cid_nat_oper_iss'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cidade_cia_aerea'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cidade_lingua'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cidade_modal_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cidade_ponto_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cidade_tab_pv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_abc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_abc_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_abc_freq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_cand'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fisc_aux_tp_prod_pauta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fisc_cofins_tp_prod_pauta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fisc_ipi_tp_prod_pauta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fisc_pis_tp_prod_pauta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_aux'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_aux_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_aux_per_sit'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_aux_ref_pauta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_cofins'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_cofins_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_cofins_zfm_cid'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_deson'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_ii'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_ii_ex'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_ii_ex_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_ii_per_sit'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_imp_orgao_fed'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_inss'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_ipi_per_sit'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_ipi_per_sit_cid'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_ipi_per_sit_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_iss_cid'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_pis'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_pis_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_pis_zfm_cid'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_trib_ipi'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_fiscal_zfm_cid'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'clas_tur_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_acordo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_bec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_ent_fator_mult'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_ent_item'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_ent_mult_di'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_rec_desp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_rec_desp_area_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_rec_desp_centro_ctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_rec_desp_cta_contab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_rec_desp_rest'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classe_recdesp_cctrl_ctacontab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classificacao_componente_pv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'classificacao_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cmp3$21572'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cob_banc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cod_gia_rs'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'codigo_ajuste_inss'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'coluna'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'com_cobranca'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'com_cobranca_cheque'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comis_acom_item_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comis_item_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comis_pas_item_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_conhec_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_conhec_frt_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_frete_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_frete_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_item_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_item_estq_reserv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_item_mov_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_item_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_item_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_item_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_item_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_item_ped_venda_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_item_req_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_num_serie'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_num_serie_item_mov_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_num_serie_item_rec_merc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_num_serie_terc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comp_ord_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compl_aplic'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'complem_plan_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'componente_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'componente_pv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comprad_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comprad_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'comprador'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_bem'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_centro_ctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_ender'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_fin_cta_publica'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_hist'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_iptu'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_iptu_rateio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_iptu_rateio_parc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_plano_cta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'compromisso_reserva'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conceito_aval'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conceito_criterio_aval_forn'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conclusao_campanha'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'concorrente_licitacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_campanha_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_cart_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_cf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_cid'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_ctrl_projeto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_ger'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_item_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_pacote_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_ped_comp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_ped_tur_prev'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_pag_reemb'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_rec_item_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_rec_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_rec_ped_tur_prev'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_rec_reemb'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cond_rec_reemb_prev'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_cart_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_conhec_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_conhec_frete_mov_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_conhec_frete_nota_fiscal'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_leit_abast'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_leit_abast_com'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_leit_abast_it'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_prod_tipo_consumo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conf_proj_majoracao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_alias_bde'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_apolo10'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_apolo2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_apolo4'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_apolo8'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_apolo_cf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_atraso_prorrog_fluxo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_bde'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_bloqueio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_campanha'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_cod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_cod_ano'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_cod_ano_mes'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_cod_ctrl_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_cod_default'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_cod_espec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_cod_hist'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_conc_banc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_conector'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_cor_acum'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_data_op_status_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_data_op_status_pv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_data_op_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_data_operacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_desconto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_dest_email'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_ecf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_ecf_cnpj'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_ecf_reg'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_fluxo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_gen_reserva'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_gera_ocorrencia'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_item_modulo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_lanc_fech_tipo_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_loc_apolo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_operacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_periodo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_rem_banc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_reserva'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_ret_banc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_tribut'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_tribut_simp_nacional'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'config_vizual_pv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'configuracao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'configuracao_check'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'configuracao_ger_lista'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'configuracao_geral'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'configuracao_geral_check'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'configuracao_lista'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'configuracao_mobile'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'configurador'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'configurador_ctrl_projeto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conhec_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conhec_frete_cte'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conhec_frete_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conhec_frt_cte_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'consulta_siscoserv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conta_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conta_fin_empresa_filial'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conta_fin_fech_fundo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conta_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conta_orcam_classe_rec_desp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conta_orcam_plano_cta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conta_parc_doc_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_ctrl_ger_paralelo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_evento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_fechamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_lanc_aprop'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_lanc_arq_anexo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_lanc_relac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_lancamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_lote_lanc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_par_exerc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_par_exerc_per'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_par_exr_per_doc_lib'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_par_exr_per_usu_lib'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_par_sld_imp_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_par_sld_imp_cta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_parametro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_rateio_gerencial'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_reduzido'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_rel'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_rel_balancete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_rel_razao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_relac_mod_orig'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_saldo_acum_cta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_saldo_bal_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_saldo_bal_cta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_saldo_cctrl_diario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_saldo_cta_diario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_saldo_mov_cctrl_old'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contab_saldo_mov_cta_old'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'conteudo_plano_ensino'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'continente'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato1'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_cei'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_classe_rec_desp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_cobranca'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_ent_contato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_entidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_entidade_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_equipamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_fat_real'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_hist_ajuste'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_hist_status'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_info_tecnica'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_info_tecnica_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_info_tecnica_func'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_int_folha'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_item_adic'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_item_ctrl_caucao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_item_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_item_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_item_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_negociacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_ordem'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_ordem_encomenda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_ordem_medicao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_ordem_parcela'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_part_oper_aplic'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_participante'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_pcta_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_plano_cta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_relac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_rgc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_saldo_servico'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_transp_rod_bens'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_vistoria'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'contrato_vistoria_foto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cor_ocup_curso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cor_ord_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cor_ord_serv_lab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cor_tempo_tipo_etapa'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cor_veiculo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'correc_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'corredor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cota_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cotac_comp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cotac_forn'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cotac_forn_anexo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cpo_tab_constr_sql'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cria_campo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cria_campo_bkp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cria_campo_bkp2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'criterio_aval_curso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'criterio_aval_forn'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cta_cont_linha_apur_imposto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cta_contab_sped'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cta_fin_bco'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrb_conhec_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrb_ent_fone'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrb_entidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_abast_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_alocacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_aluguel_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_carga_apont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_carga_item'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_carga_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_carreg'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_carreg_ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_cartao_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_caucao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_comis_vend'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_deb_cred_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_deb_cred_mov_banc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_df'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_df_modulo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_df_nfe_inut'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_df_nfe_num_rand'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_df_reser_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_df_reser_nf_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_doc_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_entsai_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_ester_apont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_ester_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_ester_prod_utiliz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_esterilizacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_exclusao_import_export'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_favoritos_usu'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_forms'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_interno'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_inv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_item_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_la_doc_encer_viagem_item'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_ajuste_inv_loc_arm'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_armaz_item_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_comp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_comp_it_ped_vd_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_comp_item_mov_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_comp_item_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_comp_item_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_comp_item_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_comp_item_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_comp_loc_armaz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_comp_ord_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_est_it_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_est_it_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_est_it_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_est_it_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_ime_doc_relac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_inv_loc_arm1'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_inv_loc_arm2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_inv_loc_arm3'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_irreg_inv_loc_arm'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_item_ctrl_esteriliz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_item_ctrl_mov_devol'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_item_mov_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_item_ord_desmont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_item_rec_merc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_item_req_mat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_la_atend_item_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_la_it_ctrl_carga_ret'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_la_item_ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_la_sim_carga_it_ret'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_loc_arm_estq_empen'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_loc_arm_it_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_loc_arm_it_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_loc_arm_it_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_loc_arm_it_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_loc_arm_itestqreserv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_loc_armaz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_mov_estq_terc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_op_ord_produc_it_alt'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_oper_op_it_req_mat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_oper_ord_produc_item'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_ord_produc_item'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_ord_produc_item_alt'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_prod_cotac_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lote_transf_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_lt_loc_arm_it_ped_vd_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_man_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_mov_devolucao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_multa_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_pdv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_pesagem'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_proced'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_proced_acao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_proced_autoriz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_proj'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_proj_est_classe_rec_desp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_proj_estimativa'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_proj_item_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_projeto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_req_entrega'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_saldo_conta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_saldo_vasil'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_seg'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_seg_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_solic_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ctrl_vasil'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cupom_fiscal'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'custo_fic_tec_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'custo_fic_tec_prod_alt'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'custo_ocor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'custo_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'custo_servico_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'custo_servico_contrato_cargo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'custo_servico_contrato_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'custo_servico_contrato_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'cxa_arq_doc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'data_item_rec_camp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'data_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dctf_parametro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ddectba_parametro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'defeito_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desc_prog_academico'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'descr_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'descr_tecn_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'descr_tecn_prod_sistema'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desenho'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desenho_agrupado'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desenho_arq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desenho_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desenho_ent_subst'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desenho_mot_lib'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desenho_subst'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desist_reserva'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desm_it_plano_produc_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'desm_item_plano_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'despesa_evento_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'despesa_ped_evento_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dessp_parametro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dest_camp_emailmark'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dest_camp_faxmark'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dest_camp_tlmark'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dest_item_ctrl_mov_devol'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dest_local_rotinas_agend'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dest_mailing'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dest_mala_direta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'det_desenho'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'det_item_ord_prop_col'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'det_item_ordem_padrao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'det_item_ordem_proposta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dev_caucao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dia_prog_ret_dest_camptl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dia_util_meta_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'diaria'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dir_grp_restr'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dir_grupo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dir_rel_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dir_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dir_usuario_mobile'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'direcionador'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'direcionador_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dirf_parametro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'disc_acervo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'disc_curso_aula_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'disc_curso_aula_ent_recurso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'disc_pre_requisito'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dispositivo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dispositivo_autorizado'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dispositivo_dash'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dispositivo_form'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dist_ender'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'distancia_cidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'diverg_fatura_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'diverg_item_fatura_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'django_migrations'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dmpl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_campanha_promocional'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_entidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_orcam_adiant'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_orcam_consorcio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_orcam_fonte_imp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_orcam_fonte_rec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_orcam_ordem'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_orcam_ordem_enc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_pcta_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_contrato_plano_cta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_ctrl_comis_vend'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_ctrl_proj_estimativa'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_ctrl_projeto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_encer_viagem'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_encer_viagem_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_encer_viagem_doc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_encer_viagem_item'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_encer_viagem_lanc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_entidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_adiant'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_bilh_conj'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_classe_rec_desp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_imp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_item_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_mix'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_proc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_rsv_it'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_fin_vinc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_licitacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_ocor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_orc_lic'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_ord_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_parc_it_contrato_orcam_ad'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_parc_it_ct_orcam_fonte_imp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_parc_it_ct_orcam_fonte_rec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_parc_it_ct_orcam_subcont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_parc_item_contrato_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_parc_item_ct_orcam_proc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_ped_venda_arq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_protocolo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_reducao_z'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_relac_dav'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_tipo_doc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_tipo_req'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'doc_verba_ctrl_projeto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'documento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'dual2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'duplicata'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_k_regk030'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_k_regk155'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_k_regk156'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_k_regk355'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_k_regk356'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_l_regl030'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_l_regl100'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_l_regl210'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_l_regl300'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m410'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_reg_m030'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_regm010'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_regm300'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_regm310'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_regm312'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_regm350'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_regm355'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_regm360'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_regm362'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_m_regm410'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_mes_vlr_optante'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn030'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn500'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn600'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn610'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn615'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn620'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn630'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn650'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn660'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_n_regn670'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_p130'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_p200'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_p300'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_p400'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_p500'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_periodo_presumido'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_t120'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_t150'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_t170'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_t181'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_u180'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_u182'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x291'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x292'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x310'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x330'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x340'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x350'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x351'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x352'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x353'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x354'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x355'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x356'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x390'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x400'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x410'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x420'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x430'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x450'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x460'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x470'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x480'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x490'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x500'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_x510'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y520'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y540'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y550'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y560'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y570'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y580'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y590'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y600'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y611'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y612'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y620'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y630'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y640'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y650'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y660'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y665'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y671'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y672'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y681'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y700'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y710'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ecf_y720'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'edge_entidade_account'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'edi_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'edi_produto1'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_base_calc_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0000'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0000_emprel'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0001'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0100'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0110'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0111'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0140'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0150'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0190'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0200'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0205'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0206'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0208'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0400'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0450'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0500'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0600'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg0990'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg1001'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg1300'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg1700'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg1900'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg1990'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg9001'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg9900'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg9990'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_reg9999'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_rega001'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_rega010'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_rega100'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_rega110'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_rega111'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_rega120'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_rega170'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_rega990'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc001'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc010'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc100'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc110'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc111'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc120'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc170'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc180'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc181'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc185'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc188'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc190'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc191'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc195'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc198'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc199'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc380'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc381'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc385'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc395'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc396'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc400'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc405'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc481'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc485'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc489'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc490'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc491'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc495'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc499'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc500'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc501'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc505'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc509'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc600'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc601'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc605'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc609'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regc990'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd001'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd010'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd100'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd101'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd105'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd111'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd200'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd201'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd205'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd209'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd300'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd309'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd350'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd359'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd500'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd501'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd505'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd509'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd600'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd601'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd605'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd609'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regd990'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf001'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf010'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf100'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf100_2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf120'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf130'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf500'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf525'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf550'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf600'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regf990'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm001'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm100'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm105'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm200'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm210'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm211'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm400'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm410'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm500'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm505'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm600'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm610'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm611'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm800'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm810'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regm990'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regp010'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_pis_cofins_regp100'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg1000'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg1070'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg2010'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg2020'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg2040'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg2050'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg2060'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg2070'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg2098'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg2099'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg5001'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg5011'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg5011_xml'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reg9000'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'efd_reinf_reglog'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'email_env'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'email_rec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'embalagem'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'embl_item_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emitente_gta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_cid_oper_fone'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_config_desconto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_ent_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_faixa_nivel'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fat_ano'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fat_ano_mes'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_aliq_cred_simples'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_cart_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_categ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_cid_tlmark'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_cno_cei'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_enquad_legal_icms'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_ent_uh_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_insc_est'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_insc_munic'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_opc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_pacote_reserva'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_pto_ref'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_socio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_fil_var_val'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_filial_certificacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_preco_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'emp_uf_oper_fone'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'empresa_filial'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'empresa_filial_aut_arq_xml'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'encer_viag_descar_bonif'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'encer_viagem'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'encer_viagem_descarga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'encer_viagem_descarga_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'encer_viagem_vasil'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'encer_viagem_vasil_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'encer_viagem_vasil_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'encer_viagem_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ender_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ender_ent_fone'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ender_ent_fone_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ender_ent_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'endereco'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_arq_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_bilh_on_line'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_bloq_tipo_rec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_cart_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_categ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_categ_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_cct_mix'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_cidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_cno_cei'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_conta_contab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_contato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_contato_desp_paga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_contato_fone'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_contato_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_cota_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_desp_paga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_disc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_disc_acervo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_disc_recurso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_disc_sala'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_doc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_doc_comp_imposto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_doc_comprobatorio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_emp_cart_fidel_comis'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_emp_fil'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_escala_cresc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_escala_cresc_faixa'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_escala_cresc_faixa_valor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_exp_profissional'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_fator_mult'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_fi'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_fone'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_fone_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_granja'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_homolog'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_item_contrato_benef'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_item_contrato_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_item_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_item_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_item_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_item_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_ligacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_ligacao_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_login'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_meta_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_mix_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_mix_tomadores'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_modal_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_negoc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_nota_fiscal'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_nota_fiscal_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_obj'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_ordem_proposta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_penalidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_periodo_canc_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_plano_ensino'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_pontuacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_pontuacao_total_doc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_prod2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_prod_23052019_1700'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_prod_23052019_1730'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_prod_certificacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_prod_codigo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_prod_reserva'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_produc_docente'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_questionario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_regiao_atuac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_regime_especial'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_reserva'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_rgc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_sistema'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_tabela_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_tipo_classe'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_tipo_compromisso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_tipo_desc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_tipo_doc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_transac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_usuario_web'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_var_val'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_vinculo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_vol_vendas'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_web'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ent_web_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade1'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_atestado'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_atestado_apres'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_aut_arq_xml'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_campanha_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_consolidada'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_item_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_item_contrato_classe'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_item_contrato_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_item_contrato_rateio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_reg_papel_imune'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'entidade_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equip_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equip_ctrl_autoriz_circ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equip_func'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equip_inst_oper'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equip_nec_plan_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equip_oper'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equip_ord_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equipamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equipamento_relac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equipe_gestor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equipe_gestor_externo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'equipe_gestor_interno'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'eqval_ponto_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'erros_sistema'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'espec_carta_cor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'espec_tit_cobranca'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'espec_veiculo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'especialista_web'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'especie_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'especific_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estado_fisico'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estag_brasil'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estag_exterior'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estag_ofer_brasil'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estag_ofer_ext'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estag_ofer_ext_nom'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estim_contab_lanc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estim_rateio_contab_lanc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estimativa_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estimativa_ctacont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estorno_atend_item_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estq_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estq_empen'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estq_loc_armaz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estq_reserv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estq_reserv_item_princ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estq_transit'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estr_item_req_mat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estrutura_custo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estrutura_custo_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estrutura_custo_centro_ctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estrutura_custo_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estrutura_custo_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'estrutura_custo_rateio_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_adiantamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_licitacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_licitacao_aviso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_lote_criacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_lote_criacao_custo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_orc_lic'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_ord_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_ord_serv_aviso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_proced'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_proced_retorno'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etapa_rec_merc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'etiq_ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'evento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'evento_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'evento_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'evento_prod_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'evento_prod_unid_med_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'eventos_lead_web'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exame_gta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exc_fluxo_cxa'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exc_pis_cofins'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exclusao_compar_nome'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exec_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exec_orcam_plan_base'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exped_agrup'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exped_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exped_ent_ar'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exped_ent_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exped_ent_prod_atend'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exped_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exped_prod_aces'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'exped_prod_atend'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'expedicao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'export_apolo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'faixa'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'faixa_autoriz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'faixa_nivel'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'faixa_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'faixa_pv_res'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'faixa_sal'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'faixa_tab_rec_simples_est'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'faixa_tab_rec_simples_fed'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura_classe_rec_desp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura_classe_rec_desp_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura_tam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura_tam_cab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fatura_tam_doc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fec_cst_etapa_lote_cria_estr'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fec_custo_cctrl_lote_criac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_cambio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_cambio_desp_banc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_cambio_parc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_conta_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_custo_etapa_lote_criac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_custo_lote_criac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_custo_lote_criacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_estq_saldo_val'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_estrut_custo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_geral_custo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_geral_custo_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_geral_custo_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_geral_custo_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fech_var_cambial'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fechamento_custo_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'feriado'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'feriado_uf_cid'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_cst_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_tec_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_tec_prod_alt'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_tec_prod_alt_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_tec_prod_alt_pos'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_tec_prod_alt_unid_princ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_tec_prod_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_tec_prod_pos'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_tec_prod_teste'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fic_tec_prod_unid_princ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ficha_cont_import'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ficha_custo_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ficha_custo_prod_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'filtro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'filtro_it'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'filtro_usu'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'filtros_web_contratos'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'filtros_web_vendas'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fin_conta_publica'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fin_conta_publica_parc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fin_nota_debito_credito'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fin_notadebcred_clasrecdesp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'finalid_veiculo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'finalidade_compra'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'finalidade_gta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_cod_coluna_rel_st'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_demonstrativo_ciap'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_guia_rec_icms'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_it_mov_prod_cred_saist'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_item_mov_prod_cred_st'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_item_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_item_nf_declarar_dia'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_item_nf_proc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_item_nf_subcont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_livro_apuracao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_livro_ent'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_livro_sai'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_mens'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_mens_aux'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_mot_res_st'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_mov_prod_cred_st'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_cf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_consorcio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_declarar_dia'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_declarar_dia_xml'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_divergencia'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_export'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_export_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_guia_rec_imp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_matriz_nac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_reg_d301'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_nf_subcont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_parc_pag_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_parc_pag_nf_consorcio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_ped_venda_diverg_hist'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_ped_venda_divergencia'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_res_apur_rec_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_res_apuracao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_resp_retencao_st'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_saldo_credito'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_saldo_credito_estorno'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_saldo_prod_cred_st'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_sql_conf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscal_sql_conf_param'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fiscalnf_fiscalnf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'folha_pagamento_func'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fonte_recurso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'forecast'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'forecast_bu'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'forecast_mensal'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'forma_pag_banco'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'formato_idioma'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'formato_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'formato_sala'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'formula_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'formularios'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'forn_item_req_comp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fornecedorweb'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'foto_acervo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'foto_entidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'foto_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'foto_item_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'foto_laudo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'foto_ord_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'foto_pat_bem'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'foto_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'foto_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fragilidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'frete_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'frete_tur_aviso'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'frete_tur_saida'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fronteira_unid_federacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'func_atividade_grupo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'func_capacidade_atend'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'func_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'func_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'func_loc_armaz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'func_oper'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'func_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'funcionario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fxa_autoriz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fxa_autoriz_val'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'fxa_autoriz_val_resp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'garantia'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'gen_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'gen_serv_empresa_filial'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'gera_num_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'gera_num_lote_tipo_lanc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'gera_num_serie'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'gerencial_config'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'giasp_parametro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade_atend_ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade_atend_item_ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade_atend_item_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade_atend_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade_cor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade_ctrl_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade_estq_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade_estq_empen'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grade_ref'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'granja'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_cia_aerea'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_emis_versao_tarifario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_func'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_imp_mailing'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_marca_prod_meta_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_marca_prod_reg_meta_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_marca_prod_vd_mtfat_classe'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_marca_prod_vend_meta_fat'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_prod_vend_meta_fat_ref'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_usu_x_config'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_usuario_mailing'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_vend'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_vend_estimulo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_vend_premio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_vend_premio_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grp_x_usuario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_bu'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_compra'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_emissao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_faturamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_marca_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_prod_caracter'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_projeto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_projeto_classe'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_projeto_linha'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_subgrupo_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'grupo_tensao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'gta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'gta_vacina'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'gta_vacina_data'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'guia_rec_gta'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'guia_rec_imp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'guia_rec_imp_cta_cont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'guia_rec_imp_des_inss'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'guia_rec_imp_des_inss_ajust'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'guia_recimp_desinss_aj_tmp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'guiarecimp_guiarecimp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_agendamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_aluno_turma'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_baixa_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_canc_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_cctrl_depara'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_cond_pag_it_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_cond_pag_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_cond_rec_it_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_cond_rec_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_doc_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_etapa_ord_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_fat_tam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_fat_tam_det'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_fat_tam_reg'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_fatura_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_ind_reaj_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_ind_reaj_contrato_aux'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_integ_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_item_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_lanc_mov_ctrl_banc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_mov_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_ocor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_ord_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_padrao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_parc_doc_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_ped_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_protesto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_regra_reaj_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_regra_reaj_contrato_aux'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_stat_aluno'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_stat_aluno_disc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'hist_ticket_apolo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'historicofaturamentobackup'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'historicooportunidadesgo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'historicoorcamentorealizado'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'historicorealizadobackup'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'historicovendasfaturamento'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'historicovendasrealbackup'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'historicovendasrealizado'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'horario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'icms_cf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'icms_mov_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'icms_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'icms_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'icms_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'icms_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'icms_rec_merc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'identificacao_ecf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'identificador_contabil'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'idioma'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'imp_arq_contab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'imp_arq_contab_lanc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'imp_arq_contab_rateio'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'imp_fic_tec'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'imp_fic_tec_item'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'imp_fic_tec_item_oper'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'imp_fic_tec_oper'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'import_apolo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'imposto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'imposto_gnre'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'in86_empresa_parametro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'in86_parametro'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'incent_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'incent_prod_unid_med'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'incentivo'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ind_economico'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ind_reaj_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ind_regra_reaj_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'ind_suspensao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inform_aidf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inform_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inform_prod_ult_comp_unid'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'infracao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inicio_fluxo_trab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inicio_fluxo_trab_proced'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inst_cobranca'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inst_oper'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inst_oper_prod_equip_oper'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_front_allotment'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_front_cond_pag'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_front_empresa_filial'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_front_entidade'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_front_faixa_pv_res'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_front_ind_economico'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_front_motivo_estorno'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_front_produto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_front_tab_pv_res'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'integ_lanc_contab'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inter_agente'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inter_clidep_centrocusto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inter_separacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inter_separacao_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'inter_separacao_randomizado'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'invent_fiscal_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'it_ctrl_carga_loc_armaz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'it_doc_parc_it_ct_orcam_proc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'it_equip_nec_plan_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'it_fec_custo_cctrl_lote_criac'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'it_grd_mat_alt_nec_plan_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'it_mov_estq_parc_contr_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'it_transf_estq_loc_armaz_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_acordo_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_adiantamento_ret'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_agenda_data_frete_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_agenda_data_pacote_tur'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_agenda_tarifario'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ajuste_dimensao_ctrl_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ajuste_inv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ajuste_inv_loc_arm'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_alt_nec_plan_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_apuracao_imposto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_atrib_aula_disc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_aux_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_aux_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_aux_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_aux_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_carta_cor'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_cf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_cob_banc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_comp_pv_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_comp_pv_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_comp_pv_orc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_comp_pv_ped_venda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_componente_pv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_config_rem_banc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_configurador'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_conhec_frete'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_conhec_frete_cte'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_conhec_frete_temp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contab_ctrl_ger_par'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contab_rel'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contab_rel_per'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contab_rel_per_lanc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contrato_caracter_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contrato_classe_recdesp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contrato_cobranca'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contrato_compet'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contrato_integ'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contrato_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contrato_orcam_sc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_contrato_ordem_encomenda'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_correc_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_cotac_comp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_cotac_forn'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_aluguel_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_carga'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_carga_base_lote'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_carga_retornavel'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_carreg'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_caucao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_ester_transflocarmaz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_esterilizacao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_inv1'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_inv2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_inv3'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_inv_loc_arm1'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_inv_loc_arm2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_inv_loc_arm3'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_man_equip'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_mov_devolucao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_projeto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_projeto_mov_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ctrl_vasil'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_descr_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_dev_caucao'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_doc_contrato'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_doc_ctrl_comis_vend'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_doc_ctrl_projeto'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_doc_fin_item_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_doc_fin_item_orcam_proc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_doc_ord_serv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_doc_parc_it_ct_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_doc_reducao_z'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_estim_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_estim_cctrl_ctacont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_estim_cctrl_ctacont_val'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_estim_cctrl_val'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_estim_ctacont'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_estim_ctacont_val'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_estq_reserv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_evento_net'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_exec_orcam'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_exec_orcam_revis'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_exec_orcam_vinc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_fatura_fin'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_fech_var_cambial'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_fechamento_custo_prod'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_ficha_emergencia'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_fin_nota_deb_cred'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_ajuste_inv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_ajuste_inv_loc_arm'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_alt_nec_plan_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_cf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_cotac_comp'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_cotac_forn'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_ctrl_inv1'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_ctrl_inv2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_ctrl_inv3'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_ctrl_inv_loc_arm1'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_ctrl_inv_loc_arm2'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_ctrl_inv_loc_arm3'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_desm_plano_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_estq_loc_armaz'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_estq_reserv'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_irreg_inv_loc_arm'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_mat_nec_ord_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_mat_nec_plan_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_mov_estq'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_mov_estq_cctrl'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_nec_plan_produc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_nf'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_nf_exc'
# The error was: ORA-00904: "IDENTITY_COLUMN": invalid identifier
# Unable to inspect table 'item_grade_orc'
