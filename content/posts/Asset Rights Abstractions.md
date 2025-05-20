
#WalletContract #DEVCON

speaker
- JOSEF J
    - Josefは、プラハのサイファーパンクコミュニティの拠点であり、Institute of Cryptoanarchyの本部である [Parallel Polis](https://paralelnipolis.cz/en) のアクティブメンバーである。IoCでは、イーサリアムのミートアップを時々開催している（2016年から）。地元の不適合者ハッカースペース [Bordel](https://bordel.space) の創設者と管理者でもある。
- NAIM
    - 現代サーカスをやっているらしいの熱い<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>

Abst.
- 5年10年15年後の onchain のモーゲージやローンに関する取り組み
- > スマートコントラクトウォレット（SCW）は、アセットコントラクトやdAppコントラクトのUXを向上させ、互換性を高める可能性を持っています。SCWをうまく活用すれば、開発者が増え続ける標準規格を統合する必要性を克服できます。その代わりに、SCWはアプリ間の互換性を高め、必要なTXの量を減らし、開発者は資産契約のカスタムやニッチなケースを扱うよりも、コアな機能に集中することができるようになります。PWN Safeはそのようなウォレットの一例で、貸し出し担保のセルフカストディを可能にします。

material: [https://archive.devcon.org/resources/6/asset-rights-abstractions-a-case-for-smart-contract-wallets.pdf](https://archive.devcon.org/resources/6/asset-rights-abstractions-a-case-for-smart-contract-wallets.pdf)

Smart contract wallets
- Proxying contract interactions bia another contract (/w extra logic)
    - pros:
        - enable advaced automation/call wrapper
            - (gnosis) safe (multisig)
            - defiSaver (external actor/bot to readjust your CDP
        - advanced identity/key handling / asset separation
            - ERC725 / 735 decentralized identity standards
            - argent (key - asset separation)
    - cons:
        - adds gas overhead
        - may require extra integrations (EIP1271etc)
- case for an asset rights layer
    - creating hooks into someoneh-else's wallet (if they consent)
    - doesnt require moving actual assets around as much
        - tackles accounting / kyc
    - self custody collateral enables defi morgage
        - have your cake and eat it too (use them while the backing a loan)
            - voting rights, gaming items/parcels, ens names
    - asset renting
        - allow someone else using your tokens w/o losing actual ownership
        - ![image](https://scrapbox.io/files/64381876089a19001c28e5b0.png)
[affiliated equirements
- Has to act as a normal contract wallet
    - call arbitrary calladata on any address
        - transfer, approve, asset utility, etc
- Enable tokenizing assets transfer rights (ATR)
    - fungible, non-fungible, and semi-fungible assets
    - enable atr token holder to transfer asset from owners wallet
    - prevent owner without an atr token to transfer / burn its assets
        - block transfer / burn calls
        - block approval calls

high level wallet design
- (gnosis) safe multisig contract wallet
    - Guard
        - checks before and after transaction
    - Module
        - enable to initiate transaction without owners approval
        - ここに、enable to lock user's assets from called transaction through other module が必要<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>

Challenge
- PWN Safeの仕組みを読んでからの方がいい
    - [https://pwn.mirror.xyz/acXg4DJglQlu61UFZufYUMy3W-lru1wPO9sXbicDSY0](https://pwn.mirror.xyz/acXg4DJglQlu61UFZufYUMy3W-lru1wPO9sXbicDSY0)
    - [[WIP_A module market for Contract wallet]] のアイデアに近いが見ている技術的部分では違かった
        - やはりGuard の脱着を標準のSafe wallet で防ぐことはできないため、Safeをベースに[[PWN Safe]] を構築している
        - アプリケーション側がファクトリーを持っているため、正しいロジックを持つwalletかどうかを確認できるようにしている
            - この仕様だとアプリケーション毎に独自のインターフェースを持つSafe walletが生まれてしまう<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
            - [[App-specific CW will be as chaotic as App Embed Wallet]]
- approval issue while minting an atr token
    - check that collection hasnot approved address before minting atr token
    - 4 type of approval
        - erc20: approve(amount)
        - erc721: approve(id) + setApprovalForAll(address)
        - erc1155: setApprovalForAll(address)
    - only erc721 - aprove(id) has a getter function for aproved address
        - all approve calls are done through wallet
            - wallet can track them
- stalking attack
    - Put victims wallet into invalid tokenized balance state
        - Victim cannot execute any transaction
            - would revert on Insufficient tokenized balance error
    - 2 types of transfer
        - Claim
            - to ATR token holder address
        - Transfer
            - to any address, but need recipient permission
    - The attack can still be executed, but much harder
        - Functions to recover from this attack
- EIP-1271
    - wallet needs to "pre-approve" hash
- gas overhead
    - minting atr token has constant overhead
    - transferring asset via atr token has linear overhead depenfing on a number of tokenized assets in a wallet
- non standard assets
    - security isseue for atr token holder when asset defines non-standard transfer or approve function
- not possible to use delegatecalls

