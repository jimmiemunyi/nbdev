# Autogenerated by nbdev

d = { 'settings': { 'audience': 'Developers',
                'author': 'Jeremy Howard and Hamel Husain',
                'author_email': 'j@fast.ai',
                'black_formatting': 'False',
                'branch': 'master',
                'console_scripts': 'nbdev_create_config=nbdev.read:nbdev_create_config\n'
                                   'nbdev_update=nbdev.sync:nbdev_update\n'
                                   'nbdev_export=nbdev.doclinks:nbdev_export\n'
                                   'nbdev_fix=nbdev.merge:nbdev_fix\n'
                                   'nbdev_trust=nbdev.clean:nbdev_trust\n'
                                   'nbdev_clean=nbdev.clean:nbdev_clean\n'
                                   'nbdev_install_hooks=nbdev.clean:nbdev_install_hooks\n'
                                   'nbdev_filter=nbdev.cli:nbdev_filter\n'
                                   'nbdev_quarto=nbdev.cli:nbdev_quarto\n'
                                   'nbdev_ghp_deploy=nbdev.cli:nbdev_ghp_deploy\n'
                                   'nbdev_sidebar=nbdev.cli:nbdev_sidebar\n'
                                   'nbdev_test=nbdev.test:nbdev_test\n'
                                   'nbdev_bump_version=nbdev.cli:nbdev_bump_version\n'
                                   'nbdev_new=nbdev.cli:nbdev_new\n'
                                   'nbdev_migrate_directives=nbdev.migrate:nbdev_migrate_directives\n'
                                   'nbdev_install_quarto=nbdev.shortcuts:install_quarto\n'
                                   'nbdev_install=nbdev.shortcuts:install\n'
                                   'nbdev_docs=nbdev.shortcuts:docs\n'
                                   'nbdev_preview=nbdev.shortcuts:preview\n'
                                   'nbdev_deploy=nbdev.shortcuts:deploy\n'
                                   'nbdev_pypi=nbdev.shortcuts:pypi\n'
                                   'nbdev_conda=nbdev.shortcuts:conda\n'
                                   'nbdev_release=nbdev.shortcuts:release\n'
                                   'nbdev_prepare=nbdev.shortcuts:prepare\n'
                                   'nbdev_help=nbdev.shortcuts:chelp',
                'copyright': '2020 onwards, Jeremy Howard',
                'custom_sidebar': 'True',
                'description': 'Create delightful software with Jupyter Notebooks',
                'dev_requirements': 'nbdev-numpy\nnbdev-stdlib\npandas\nmatplotlib\nipython\nblack\nghapi',
                'doc_baseurl': '/',
                'doc_host': 'https://nbdev.fast.ai',
                'doc_path': '_docs',
                'git_url': 'https://github.com/fastai/nbdev',
                'host': 'github',
                'keywords': 'nbdev fastai jupyter notebook export',
                'language': 'English',
                'lib_name': 'nbdev',
                'lib_path': 'nbdev',
                'license': 'apache2',
                'min_python': '3.7',
                'nbs_path': 'nbs',
                'recursive': 'False',
                'repo': 'nbdev',
                'requirements': 'fastcore>=1.5.8 execnb astunparse',
                'status': '2',
                'title': 'nbdev',
                'tst_flags': 'notest',
                'user': 'fastai',
                'version': '2.0.0'},
  'syms': { 'nbdev.clean': { 'nbdev.clean.clean_nb': 'https://nbdev.fast.ai/clean#clean_nb',
                             'nbdev.clean.nbdev_clean': 'https://nbdev.fast.ai/clean#nbdev_clean',
                             'nbdev.clean.nbdev_install_hooks': 'https://nbdev.fast.ai/clean#nbdev_install_hooks',
                             'nbdev.clean.nbdev_trust': 'https://nbdev.fast.ai/clean#nbdev_trust',
                             'nbdev.clean.process_write': 'https://nbdev.fast.ai/clean#process_write'},
            'nbdev.cli': { 'nbdev.cli.FilterDefaults': 'https://nbdev.fast.ai/cli#FilterDefaults',
                           'nbdev.cli.FilterDefaults.base_postprocs': 'https://nbdev.fast.ai/cli#FilterDefaults.base_postprocs',
                           'nbdev.cli.FilterDefaults.base_preprocs': 'https://nbdev.fast.ai/cli#FilterDefaults.base_preprocs',
                           'nbdev.cli.FilterDefaults.base_procs': 'https://nbdev.fast.ai/cli#FilterDefaults.base_procs',
                           'nbdev.cli.FilterDefaults.nb_proc': 'https://nbdev.fast.ai/cli#FilterDefaults.nb_proc',
                           'nbdev.cli.FilterDefaults.postprocs': 'https://nbdev.fast.ai/cli#FilterDefaults.postprocs',
                           'nbdev.cli.FilterDefaults.preprocs': 'https://nbdev.fast.ai/cli#FilterDefaults.preprocs',
                           'nbdev.cli.FilterDefaults.procs': 'https://nbdev.fast.ai/cli#FilterDefaults.procs',
                           'nbdev.cli.bump_version': 'https://nbdev.fast.ai/cli#bump_version',
                           'nbdev.cli.extract_tgz': 'https://nbdev.fast.ai/cli#extract_tgz',
                           'nbdev.cli.nbdev_bump_version': 'https://nbdev.fast.ai/cli#nbdev_bump_version',
                           'nbdev.cli.nbdev_filter': 'https://nbdev.fast.ai/cli#nbdev_filter',
                           'nbdev.cli.nbdev_ghp_deploy': 'https://nbdev.fast.ai/cli#nbdev_ghp_deploy',
                           'nbdev.cli.nbdev_new': 'https://nbdev.fast.ai/cli#nbdev_new',
                           'nbdev.cli.nbdev_quarto': 'https://nbdev.fast.ai/cli#nbdev_quarto',
                           'nbdev.cli.nbdev_sidebar': 'https://nbdev.fast.ai/cli#nbdev_sidebar',
                           'nbdev.cli.prompt_user': 'https://nbdev.fast.ai/cli#prompt_user',
                           'nbdev.cli.refresh_quarto_yml': 'https://nbdev.fast.ai/cli#refresh_quarto_yml',
                           'nbdev.cli.update_version': 'https://nbdev.fast.ai/cli#update_version'},
            'nbdev.doclinks': { 'nbdev.doclinks.DocLinks': 'https://nbdev.fast.ai/doclinks#DocLinks',
                                'nbdev.doclinks.DocLinks.build_index': 'https://nbdev.fast.ai/doclinks#DocLinks.build_index',
                                'nbdev.doclinks.DocLinks.update_syms': 'https://nbdev.fast.ai/doclinks#DocLinks.update_syms',
                                'nbdev.doclinks.DocLinks.write_nbdev_idx': 'https://nbdev.fast.ai/doclinks#DocLinks.write_nbdev_idx',
                                'nbdev.doclinks.NbdevLookup': 'https://nbdev.fast.ai/doclinks#NbdevLookup',
                                'nbdev.doclinks.NbdevLookup._link_sym': 'https://nbdev.fast.ai/doclinks#NbdevLookup._link_sym',
                                'nbdev.doclinks.NbdevLookup.link_line': 'https://nbdev.fast.ai/doclinks#NbdevLookup.link_line',
                                'nbdev.doclinks.NbdevLookup.linkify': 'https://nbdev.fast.ai/doclinks#NbdevLookup.linkify',
                                'nbdev.doclinks.build_modidx': 'https://nbdev.fast.ai/doclinks#build_modidx',
                                'nbdev.doclinks.get_patch_name': 'https://nbdev.fast.ai/doclinks#get_patch_name',
                                'nbdev.doclinks.nbdev_export': 'https://nbdev.fast.ai/doclinks#nbdev_export',
                                'nbdev.doclinks.nbglob': 'https://nbdev.fast.ai/doclinks#nbglob'},
            'nbdev.export': { 'nbdev.export.ExportModuleProc': 'https://nbdev.fast.ai/export#ExportModuleProc',
                              'nbdev.export.black_format': 'https://nbdev.fast.ai/export#black_format',
                              'nbdev.export.create_modules': 'https://nbdev.fast.ai/export#create_modules',
                              'nbdev.export.nb_export': 'https://nbdev.fast.ai/export#nb_export'},
            'nbdev.extract_attachments': { 'nbdev.extract_attachments.ExtractAttachmentsPreprocessor': 'https://nbdev.fast.ai/extract_attachments#ExtractAttachmentsPreprocessor',
                                           'nbdev.extract_attachments.ExtractAttachmentsPreprocessor.preprocess_cell': 'https://nbdev.fast.ai/extract_attachments#ExtractAttachmentsPreprocessor.preprocess_cell'},
            'nbdev.imports': {},
            'nbdev.maker': { 'nbdev.maker.ModuleMaker': 'https://nbdev.fast.ai/maker#ModuleMaker',
                             'nbdev.maker.ModuleMaker._last_future': 'https://nbdev.fast.ai/maker#ModuleMaker._last_future',
                             'nbdev.maker.ModuleMaker._make_exists': 'https://nbdev.fast.ai/maker#ModuleMaker._make_exists',
                             'nbdev.maker.ModuleMaker._update_all': 'https://nbdev.fast.ai/maker#ModuleMaker._update_all',
                             'nbdev.maker.ModuleMaker.make': 'https://nbdev.fast.ai/maker#ModuleMaker.make',
                             'nbdev.maker.ModuleMaker.make_all': 'https://nbdev.fast.ai/maker#ModuleMaker.make_all',
                             'nbdev.maker.NbCell.import2relative': 'https://nbdev.fast.ai/maker#NbCell.import2relative',
                             'nbdev.maker.basic_export_nb2': 'https://nbdev.fast.ai/maker#basic_export_nb2',
                             'nbdev.maker.decor_id': 'https://nbdev.fast.ai/maker#decor_id',
                             'nbdev.maker.find_var': 'https://nbdev.fast.ai/maker#find_var',
                             'nbdev.maker.make_code_cell': 'https://nbdev.fast.ai/maker#make_code_cell',
                             'nbdev.maker.make_code_cells': 'https://nbdev.fast.ai/maker#make_code_cells',
                             'nbdev.maker.read_var': 'https://nbdev.fast.ai/maker#read_var',
                             'nbdev.maker.relative_import': 'https://nbdev.fast.ai/maker#relative_import',
                             'nbdev.maker.retr_exports': 'https://nbdev.fast.ai/maker#retr_exports',
                             'nbdev.maker.update_import': 'https://nbdev.fast.ai/maker#update_import',
                             'nbdev.maker.update_var': 'https://nbdev.fast.ai/maker#update_var'},
            'nbdev.merge': { 'nbdev.merge.conf_re': 'https://nbdev.fast.ai/merge#conf_re',
                             'nbdev.merge.nbdev_fix': 'https://nbdev.fast.ai/merge#nbdev_fix',
                             'nbdev.merge.unpatch': 'https://nbdev.fast.ai/merge#unpatch'},
            'nbdev.migrate': { 'nbdev.migrate.migrate_md_fm': 'https://nbdev.fast.ai/migrate#migrate_md_fm',
                               'nbdev.migrate.migrate_nb_fm': 'https://nbdev.fast.ai/migrate#migrate_nb_fm',
                               'nbdev.migrate.nbdev_migrate_directives': 'https://nbdev.fast.ai/migrate#nbdev_migrate_directives'},
            'nbdev.mkdocs': { 'nbdev.mkdocs.RmNumPrefix': 'https://nbdev.fast.ai/mkdocs#RmNumPrefix',
                              'nbdev.mkdocs.RmNumPrefix.on_pre_page': 'https://nbdev.fast.ai/mkdocs#RmNumPrefix.on_pre_page'},
            'nbdev.process': { 'nbdev.process.NBProcessor': 'https://nbdev.fast.ai/process#NBProcessor',
                               'nbdev.process.NBProcessor.process': 'https://nbdev.fast.ai/process#NBProcessor.process',
                               'nbdev.process.extract_directives': 'https://nbdev.fast.ai/process#extract_directives',
                               'nbdev.process.first_code_ln': 'https://nbdev.fast.ai/process#first_code_ln',
                               'nbdev.process.instantiate': 'https://nbdev.fast.ai/process#instantiate',
                               'nbdev.process.langs': 'https://nbdev.fast.ai/process#langs',
                               'nbdev.process.nb_lang': 'https://nbdev.fast.ai/process#nb_lang',
                               'nbdev.process.opt_set': 'https://nbdev.fast.ai/process#opt_set'},
            'nbdev.processors': { 'nbdev.processors.DEFAULT_FM_KEYS': 'https://nbdev.fast.ai/processors#DEFAULT_FM_KEYS',
                                  'nbdev.processors.add_links': 'https://nbdev.fast.ai/processors#add_links',
                                  'nbdev.processors.add_show_docs': 'https://nbdev.fast.ai/processors#add_show_docs',
                                  'nbdev.processors.cell_lang': 'https://nbdev.fast.ai/processors#cell_lang',
                                  'nbdev.processors.clean_magics': 'https://nbdev.fast.ai/processors#clean_magics',
                                  'nbdev.processors.clean_show_doc': 'https://nbdev.fast.ai/processors#clean_show_doc',
                                  'nbdev.processors.construct_fm': 'https://nbdev.fast.ai/processors#construct_fm',
                                  'nbdev.processors.exec_show_docs': 'https://nbdev.fast.ai/processors#exec_show_docs',
                                  'nbdev.processors.filter_stream_': 'https://nbdev.fast.ai/processors#filter_stream_',
                                  'nbdev.processors.hide_': 'https://nbdev.fast.ai/processors#hide_',
                                  'nbdev.processors.hide_line': 'https://nbdev.fast.ai/processors#hide_line',
                                  'nbdev.processors.infer_frontmatter': 'https://nbdev.fast.ai/processors#infer_frontmatter',
                                  'nbdev.processors.insert_frontmatter': 'https://nbdev.fast.ai/processors#insert_frontmatter',
                                  'nbdev.processors.insert_warning': 'https://nbdev.fast.ai/processors#insert_warning',
                                  'nbdev.processors.is_frontmatter': 'https://nbdev.fast.ai/processors#is_frontmatter',
                                  'nbdev.processors.lang_identify': 'https://nbdev.fast.ai/processors#lang_identify',
                                  'nbdev.processors.nb_fmdict': 'https://nbdev.fast.ai/processors#nb_fmdict',
                                  'nbdev.processors.nbflags_': 'https://nbdev.fast.ai/processors#nbflags_',
                                  'nbdev.processors.populate_language': 'https://nbdev.fast.ai/processors#populate_language',
                                  'nbdev.processors.rm_export': 'https://nbdev.fast.ai/processors#rm_export',
                                  'nbdev.processors.rm_header_dash': 'https://nbdev.fast.ai/processors#rm_header_dash',
                                  'nbdev.processors.strip_ansi': 'https://nbdev.fast.ai/processors#strip_ansi',
                                  'nbdev.processors.strip_hidden_metadata': 'https://nbdev.fast.ai/processors#strip_hidden_metadata'},
            'nbdev.read': { 'nbdev.read.add_init': 'https://nbdev.fast.ai/read#add_init',
                            'nbdev.read.basic_export_nb': 'https://nbdev.fast.ai/read#basic_export_nb',
                            'nbdev.read.config_key': 'https://nbdev.fast.ai/read#config_key',
                            'nbdev.read.create_output': 'https://nbdev.fast.ai/read#create_output',
                            'nbdev.read.get_config': 'https://nbdev.fast.ai/read#get_config',
                            'nbdev.read.mk_cell': 'https://nbdev.fast.ai/read#mk_cell',
                            'nbdev.read.nbdev_create_config': 'https://nbdev.fast.ai/read#nbdev_create_config',
                            'nbdev.read.write_cells': 'https://nbdev.fast.ai/read#write_cells'},
            'nbdev.shortcuts': { 'nbdev.shortcuts.BASE_QUARTO_URL': 'https://nbdev.fast.ai/shortcuts#BASE_QUARTO_URL',
                                 'nbdev.shortcuts.chelp': 'https://nbdev.fast.ai/shortcuts#chelp',
                                 'nbdev.shortcuts.conda': 'https://nbdev.fast.ai/shortcuts#conda',
                                 'nbdev.shortcuts.deploy': 'https://nbdev.fast.ai/shortcuts#deploy',
                                 'nbdev.shortcuts.docs': 'https://nbdev.fast.ai/shortcuts#docs',
                                 'nbdev.shortcuts.install': 'https://nbdev.fast.ai/shortcuts#install',
                                 'nbdev.shortcuts.install_quarto': 'https://nbdev.fast.ai/shortcuts#install_quarto',
                                 'nbdev.shortcuts.prepare': 'https://nbdev.fast.ai/shortcuts#prepare',
                                 'nbdev.shortcuts.preview': 'https://nbdev.fast.ai/shortcuts#preview',
                                 'nbdev.shortcuts.pypi': 'https://nbdev.fast.ai/shortcuts#pypi',
                                 'nbdev.shortcuts.release': 'https://nbdev.fast.ai/shortcuts#release'},
            'nbdev.showdoc': { 'nbdev.showdoc.BasicHtmlRenderer': 'https://nbdev.fast.ai/showdoc#BasicHtmlRenderer',
                               'nbdev.showdoc.BasicMarkdownRenderer': 'https://nbdev.fast.ai/showdoc#BasicMarkdownRenderer',
                               'nbdev.showdoc.DocmentTbl': 'https://nbdev.fast.ai/showdoc#DocmentTbl',
                               'nbdev.showdoc.DocmentTbl.has_docment': 'https://nbdev.fast.ai/showdoc#DocmentTbl.has_docment',
                               'nbdev.showdoc.DocmentTbl.has_return': 'https://nbdev.fast.ai/showdoc#DocmentTbl.has_return',
                               'nbdev.showdoc.DocmentTbl.hdr_str': 'https://nbdev.fast.ai/showdoc#DocmentTbl.hdr_str',
                               'nbdev.showdoc.DocmentTbl.params_str': 'https://nbdev.fast.ai/showdoc#DocmentTbl.params_str',
                               'nbdev.showdoc.DocmentTbl.return_str': 'https://nbdev.fast.ai/showdoc#DocmentTbl.return_str',
                               'nbdev.showdoc.ShowDocRenderer': 'https://nbdev.fast.ai/showdoc#ShowDocRenderer',
                               'nbdev.showdoc.colab_link': 'https://nbdev.fast.ai/showdoc#colab_link',
                               'nbdev.showdoc.show_doc': 'https://nbdev.fast.ai/showdoc#show_doc',
                               'nbdev.showdoc.showdoc_nm': 'https://nbdev.fast.ai/showdoc#showdoc_nm'},
            'nbdev.sync': { 'nbdev.sync.absolute_import': 'https://nbdev.fast.ai/sync#absolute_import',
                            'nbdev.sync.nbdev_update': 'https://nbdev.fast.ai/sync#nbdev_update'},
            'nbdev.test': {'nbdev.test.nbdev_test': 'https://nbdev.fast.ai/test#nbdev_test', 'nbdev.test.test_nb': 'https://nbdev.fast.ai/test#test_nb'},
            'nbdev.tutorial': { 'nbdev.tutorial.HelloSayer': 'https://nbdev.fast.ai/tutorial#HelloSayer',
                                'nbdev.tutorial.HelloSayer.say': 'https://nbdev.fast.ai/tutorial#HelloSayer.say',
                                'nbdev.tutorial.say_hello': 'https://nbdev.fast.ai/tutorial#say_hello'}}}