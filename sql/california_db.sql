PGDMP     4    6                {         
   california    15.2    15.2 
    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16398 
   california    DATABASE     �   CREATE DATABASE california WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE california;
                postgres    false            �            1259    16454    alternative_data    TABLE     �  CREATE TABLE public.alternative_data (
    date date NOT NULL,
    search_hous_bubble numeric(6,4),
    search_pand_assist numeric(6,4),
    search_pfl numeric(6,4),
    search_recession numeric(6,4),
    search_unemp numeric(6,4),
    us_consumer_sentiment numeric(4,2),
    mob_leisure numeric(8,6),
    mob_groc_pharm numeric(8,6),
    mob_parks numeric(8,6),
    mob_transit numeric(8,6),
    mob_workplaces numeric(8,6),
    mob_residential numeric(8,6)
);
 $   DROP TABLE public.alternative_data;
       public         heap    postgres    false            �            1259    16444    traditional_data    TABLE     ,  CREATE TABLE public.traditional_data (
    date date NOT NULL,
    gdp numeric(8,1),
    employment numeric(11,4),
    expenditure numeric(10,3),
    exports numeric(12,6),
    imports numeric(12,6),
    min_wage numeric(4,2),
    personal_income numeric(8,1),
    disposable_income numeric(10,3)
);
 $   DROP TABLE public.traditional_data;
       public         heap    postgres    false            �          0    16454    alternative_data 
   TABLE DATA           �   COPY public.alternative_data (date, search_hous_bubble, search_pand_assist, search_pfl, search_recession, search_unemp, us_consumer_sentiment, mob_leisure, mob_groc_pharm, mob_parks, mob_transit, mob_workplaces, mob_residential) FROM stdin;
    public          postgres    false    215          �          0    16444    traditional_data 
   TABLE DATA           �   COPY public.traditional_data (date, gdp, employment, expenditure, exports, imports, min_wage, personal_income, disposable_income) FROM stdin;
    public          postgres    false    214           k           2606    16458 &   alternative_data alternative_data_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.alternative_data
    ADD CONSTRAINT alternative_data_pkey PRIMARY KEY (date);
 P   ALTER TABLE ONLY public.alternative_data DROP CONSTRAINT alternative_data_pkey;
       public            postgres    false    215            i           2606    16448 &   traditional_data traditional_data_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.traditional_data
    ADD CONSTRAINT traditional_data_pkey PRIMARY KEY (date);
 P   ALTER TABLE ONLY public.traditional_data DROP CONSTRAINT traditional_data_pkey;
       public            postgres    false    214            �   �  x��X[��8���K) !@����ϱ�B�R��ttD��䝤L �~��T�{A�[/(�Պ���"�������c�W�06��Zh
syS����0׫b��ޠO��B����a�Rce��'��wf(2����I|���c~w�E�|�*�L�#
����$_(�dwb^o���#����
1��݊5%��*��^�7y]�������x�\}ů��h/k����/��Q�UGĦnگmL��߶��F�uT��ԡ��N�2&����t�:0�`���{[1�kߵE��n�{�J�l1B�&�7[�Q�ާ��?x��y���=��E��7�W�'��";cc�0�Q��0Тx���X��u���afP'w꼿FQ�� ����Zz�O���'gpoU_Q�R}�y�r��	;����֔}��'���M,�D%��v.�V+˒<`8/y�DLV�>����c���7�'m<�7'����(9�k�"[D�e�(U��K}��r%�%�{����WH#O)�>��3I�Zo�����H�I"�2�g�P	?5^��to<_`��3�q�-Z*B����-_�g���Ѭy���LN�1�<��-�ɇ���)��|g�ӕ���z��=���;�u{NL�ʉ�(y�Ȓ�s�h���17�����6�*8��ZMg���;1g��~)���i,��e��h�B��&Fq�,���%]D����كF6&ו�^&���b�CE�awU��`k�b��E�!D1Z�Fާo_��Yȼ��W2Z�57��J�KF�Y)dQ�ip;*��@���!��`���>�m�D7�m$t�h57=G�)���$xC�w��5כ�����7v0�Fѕ�,25��.K�D[��δPOFz�ߊq2�ea��|�I�[t޻�Lu������({�����y�$Mk%�=���V�U�<��pfR�D�AߵC�������`�*�8V���/���Y:��)��zl�"��#�ϙ3+�R�x���V�w��6H���jG��+���A�O_'� _](��Xj�B$��hj-۔��8�o�_s�Yz���"ݔ�R�c��O���3�uT�:�8��eH(:6�Ԧm�:����o��5�Y�c�0�ϛA�,J�W������/"�1�ö�#��)Aa2�v]ػ��#�A)l~>)�G6آr��E�bj8#0�BY��m�9V�4;�͓�A GB�������cU��      �   F
  x�m�[�$7D�k�b��H��
f���A��j���uw
A�$��s�'�\2J�^R�D[��k�W-bu$q�j�RR���ՋzIe������2T���O��m�[��&	�,)�����i,�!�k����PM�	/��K.EFO~I�c�1᫵��*A�K�խ>��l�@����$�9��?�'�H'��w�	��4I#����^[����{��z�?/=�}�G���e������<�Q��{.�?�����.-Yv+���Ҙ�j�I�-[jVU��-��ͬ��8��#��Or�ɽ�ZS^r(��oBnS.ޮѼ[��F���R�����YJگȺ-�4h�GۄW�O�Z�k�ڈ@��f��R\��<J���j�A|�v��0��J�@�\)��R�@��[*�,�8������,��j����/񞓩v�Ps#��s��Ox���X��!�$��v�ޛ$��Q�(�h4�����4�Ư� ��z��՚��N�2�m�z��%j\j�T���0��>`ՠw��·]��|�w2:QBLs��Du��uGX5����Qp���j0x4k��HQ�� hi�mt	���5��u@���u���#j jB���ܠs.��ƾA���f:��jԐ��QX�C�ԣZ��7�ADe�^I ,��B�s���;��M�>�ӥ�ޢ�*"�����`| i��%o���CS���L��N�4rFZ3Y���PD�s#�#�o��"L��&��Vu���W��C(��|�0h�&����ed��O���EIKʓ�_�h�@�k�P�����t�f�.p*P��6��t�;A�M��	�Z�Ӛ��� TIc<8S<A���M��ɡ���ӠnE_'9�rx���K����";S���SZ
�nr�~�F�|:S��6��Z��m� �nw"�q9s�AFp��?�?�{��y:��R�A�2S���=�S��p�02H]�Z��� D[R�l���E���DkZ��n�]4��q���xjf16(�<mHw"�:�D(W�.��2���g�'�@cn�O��2��f��^�^��h���9,�||G����+ޘf}:��4�mD��oӷ���Ì�Ű)�ɳiX�AUҰ��7�M�F�w��	A#���'���G�9�T9&lt6v!���ɷ��A����TN��9H���d[c�;�[�a�Ӈe4-1��+GN��"1"�x�y	��a�h;6�=����y���[�����o?]}�hu�ψ⻌J�z�u���3D���^�Vc�F� G�hu~Ã|�{nt�=�������؁w~ۦ��0�>�h�^a�pT�����ոr(y�?�+%LW~���a�%O��B�:� g��./�S��^���r���oКT{�*��C��R�mI�\Q<I������9=�C����:A^����G"V���|Y���#f���c�4@��Y*�����x�|�_R��$gM*�?1��-,/�/w7�aLN嬟_�4?J�`�o>�B7��[������\��*T_���:��3KKT�ٰv��O��8����(ƙ颥����w�Z���vj�3;�_Vy%����w-���Ǵ/�Bt�3���kA,d7FM��7��c�aQ���	q��OTL$E�-&��5�x�����:�G�M)Ĺ���G�%6��%Y*�p���B� ����w���N��NA��<$��qoao2�
9��~s�|����_l�P��������tƹ����E�Q�6�K���������Dz�߰6�L�`�v�_5� ��������Y�������z�1=$�_|A#�P|���T����(�1���;���;mk$bM���T"V&JX�lH_�P�z�#����3,�ϐ��Zk��ov?�D���I�/�����ⰅO�ڤ�wo�gn���\>ّ�^|>�썴4�g"^�
��i�Ǎ�چ���+�M���?�{�>+yx�0NA��>�5J�(��>`���!_�B�
��5�r��g��ns���|�(�F��Ʃ ���vz\�W�}��LFG5PA��e�Z�WOtqן�s�|k>��6�o��/�5fC��ỐIL�} cG��z��O↦��a %.�dͣ�;��<�M�@�u�7�[����k:��r?ik�����TC�i\�%V��\�$۽Ya����x�c����v�v�l1�ٱ��Cp6����4����Q�-�r��7i��:��~<u��&r�cԷ�p$l��1��3����	�u�c�pf?��i/걲� �".��y:�Zۋ|��6ۋ�η����!7���ӣ��1��c�	?Ds!*桞���խ���ۨ��<p8��w���`t�v���0Q瑡y������:h��|Yc[쾝�W���8ѳk�?���|��E���tpNm�O|G/a(P�ؼ�^�WAC�D@��gX>������3�|�x���J��_P���0�oP��8Mq��;�F���F�����v�i7|]޶��O-�a�<̷�?[V���_�m�a���U1w"��9����J�s�x���1��8�|V7�Э��wJ�X3䝒�1�g���?��d��A     