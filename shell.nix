{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
	 nativeBuildInputs = with pkgs; [
    		python3
    		python311Packages.django
   		python311Packages.pillow
  	];
  	shellHook = ''
    		echo "Shell prepared!"
  	'';
}
