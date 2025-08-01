# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAKE_COLOR_MAP_METADATA = Metadata(
    id="74bc2813713e1afd72d384800e82892e19f26459.boutiques",
    name="MakeColorMap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


MakeColorMapParameters = typing.TypedDict('MakeColorMapParameters', {
    "__STYXTYPE__": typing.Literal["MakeColorMap"],
    "fiducials_ncol": typing.NotRequired[InputPathType | None],
    "fiducials": typing.NotRequired[InputPathType | None],
    "num_colors": typing.NotRequired[float | None],
    "std_mapname": typing.NotRequired[str | None],
    "palette_file": typing.NotRequired[InputPathType | None],
    "cmap_name": typing.NotRequired[str | None],
    "fscolut_labels": typing.NotRequired[list[float] | None],
    "fscolut_file": typing.NotRequired[InputPathType | None],
    "afni_hex": typing.NotRequired[str | None],
    "afni_hex_complete": typing.NotRequired[str | None],
    "suma_colormap": typing.NotRequired[str | None],
    "user_colut_file": typing.NotRequired[InputPathType | None],
    "sdset": typing.NotRequired[InputPathType | None],
    "sdset_prefix": typing.NotRequired[str | None],
    "flipupdown": bool,
    "skip_last": bool,
    "show_fscolut": bool,
    "help_flag": bool,
    "help_full_flag": bool,
    "flip_map_updside_down": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "MakeColorMap": make_color_map_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "MakeColorMap": make_color_map_outputs,
    }.get(t)


class MakeColorMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_color_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    afni_hex_output_prefix: OutputPathType | None
    """Prefix for individual color values in AFNI Hex format."""
    palette_file_output: OutputPathType
    """Example palette file output."""


def make_color_map_params(
    fiducials_ncol: InputPathType | None = None,
    fiducials: InputPathType | None = None,
    num_colors: float | None = None,
    std_mapname: str | None = None,
    palette_file: InputPathType | None = None,
    cmap_name: str | None = None,
    fscolut_labels: list[float] | None = None,
    fscolut_file: InputPathType | None = None,
    afni_hex: str | None = None,
    afni_hex_complete: str | None = None,
    suma_colormap: str | None = None,
    user_colut_file: InputPathType | None = None,
    sdset: InputPathType | None = None,
    sdset_prefix: str | None = None,
    flipupdown: bool = False,
    skip_last: bool = False,
    show_fscolut: bool = False,
    help_flag: bool = False,
    help_full_flag: bool = False,
    flip_map_updside_down: bool = False,
) -> MakeColorMapParameters:
    """
    Build parameters.
    
    Args:
        fiducials_ncol: Fiducial colors and their indices in the color map are\
            listed in file Fiducials_Ncol.
        fiducials: Fiducial colors are listed in an ascii file Fiducials.
        num_colors: Total number of colors in the color map.
        std_mapname: Returns one of SUMA's standard colormaps.
        palette_file: Specify the palette file for colormap.
        cmap_name: Specify the colormap name.
        fscolut_labels: Get AFNI/SUMA colormaps of FreeSurfer colors indexed\
            between lbl0 and lbl1.
        fscolut_file: Use color LUT file FS_COL_LUT.
        afni_hex: Afni Hex format. Use this option if you want a color map\
            formatted to fit in AFNI's .afnirc file.
        afni_hex_complete: Afni Hex format, ready to go into pbardefs.h.
        suma_colormap: Write colormap in SUMA's format.
        user_colut_file: Provide a user's own color lookup file.
        sdset: Add colormap to surface-based dataset DSET, making it a labeled\
            dataset.
        sdset_prefix: Prefix of dset for writing labeled version of DSET.
        flipupdown: Flip the map upside down.
        skip_last: If used, the last color in the Fiducial list is omitted.
        show_fscolut: Show all of the FreeSurfer LUT.
        help_flag: Displays the help message.
        help_full_flag: Displays the help message.
        flip_map_updside_down: Flip the map upside down.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "MakeColorMap",
        "flipupdown": flipupdown,
        "skip_last": skip_last,
        "show_fscolut": show_fscolut,
        "help_flag": help_flag,
        "help_full_flag": help_full_flag,
        "flip_map_updside_down": flip_map_updside_down,
    }
    if fiducials_ncol is not None:
        params["fiducials_ncol"] = fiducials_ncol
    if fiducials is not None:
        params["fiducials"] = fiducials
    if num_colors is not None:
        params["num_colors"] = num_colors
    if std_mapname is not None:
        params["std_mapname"] = std_mapname
    if palette_file is not None:
        params["palette_file"] = palette_file
    if cmap_name is not None:
        params["cmap_name"] = cmap_name
    if fscolut_labels is not None:
        params["fscolut_labels"] = fscolut_labels
    if fscolut_file is not None:
        params["fscolut_file"] = fscolut_file
    if afni_hex is not None:
        params["afni_hex"] = afni_hex
    if afni_hex_complete is not None:
        params["afni_hex_complete"] = afni_hex_complete
    if suma_colormap is not None:
        params["suma_colormap"] = suma_colormap
    if user_colut_file is not None:
        params["user_colut_file"] = user_colut_file
    if sdset is not None:
        params["sdset"] = sdset
    if sdset_prefix is not None:
        params["sdset_prefix"] = sdset_prefix
    return params


def make_color_map_cargs(
    params: MakeColorMapParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("MakeColorMap")
    if params.get("fiducials_ncol") is not None:
        cargs.extend([
            "-fn",
            execution.input_file(params.get("fiducials_ncol"))
        ])
    if params.get("fiducials") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("fiducials"))
        ])
    if params.get("num_colors") is not None:
        cargs.extend([
            "-nc",
            str(params.get("num_colors"))
        ])
    if params.get("std_mapname") is not None:
        cargs.extend([
            "-std",
            params.get("std_mapname")
        ])
    if params.get("palette_file") is not None:
        cargs.extend([
            "-cmapdb",
            execution.input_file(params.get("palette_file"))
        ])
    if params.get("cmap_name") is not None:
        cargs.extend([
            "-cmap",
            params.get("cmap_name")
        ])
    if params.get("fscolut_labels") is not None:
        cargs.extend([
            "-fscolut",
            *map(str, params.get("fscolut_labels"))
        ])
    if params.get("fscolut_file") is not None:
        cargs.extend([
            "-fscolutfile",
            execution.input_file(params.get("fscolut_file"))
        ])
    if params.get("afni_hex") is not None:
        cargs.extend([
            "-ah",
            params.get("afni_hex")
        ])
    if params.get("afni_hex_complete") is not None:
        cargs.extend([
            "-ahc",
            params.get("afni_hex_complete")
        ])
    if params.get("suma_colormap") is not None:
        cargs.extend([
            "-suma_cmap",
            params.get("suma_colormap")
        ])
    if params.get("user_colut_file") is not None:
        cargs.extend([
            "-usercolutfile",
            execution.input_file(params.get("user_colut_file"))
        ])
    if params.get("sdset") is not None:
        cargs.extend([
            "-sdset",
            execution.input_file(params.get("sdset"))
        ])
    if params.get("sdset_prefix") is not None:
        cargs.extend([
            "-sdset_prefix",
            params.get("sdset_prefix")
        ])
    if params.get("flipupdown"):
        cargs.append("-flipud")
    if params.get("skip_last"):
        cargs.append("-sl")
    if params.get("show_fscolut"):
        cargs.append("-show_fscolut")
    if params.get("help_flag"):
        cargs.append("-h")
    if params.get("help_full_flag"):
        cargs.append("-help")
    if params.get("flip_map_updside_down"):
        cargs.append("-flipud")
    return cargs


def make_color_map_outputs(
    params: MakeColorMapParameters,
    execution: Execution,
) -> MakeColorMapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakeColorMapOutputs(
        root=execution.output_file("."),
        afni_hex_output_prefix=execution.output_file(params.get("afni_hex") + "_01") if (params.get("afni_hex") is not None) else None,
        palette_file_output=execution.output_file("TestPalette.pal"),
    )
    return ret


def make_color_map_execute(
    params: MakeColorMapParameters,
    execution: Execution,
) -> MakeColorMapOutputs:
    """
    Utility for creating and modifying colormaps with various formats and fiducial
    points.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakeColorMapOutputs`).
    """
    params = execution.params(params)
    cargs = make_color_map_cargs(params, execution)
    ret = make_color_map_outputs(params, execution)
    execution.run(cargs)
    return ret


def make_color_map(
    fiducials_ncol: InputPathType | None = None,
    fiducials: InputPathType | None = None,
    num_colors: float | None = None,
    std_mapname: str | None = None,
    palette_file: InputPathType | None = None,
    cmap_name: str | None = None,
    fscolut_labels: list[float] | None = None,
    fscolut_file: InputPathType | None = None,
    afni_hex: str | None = None,
    afni_hex_complete: str | None = None,
    suma_colormap: str | None = None,
    user_colut_file: InputPathType | None = None,
    sdset: InputPathType | None = None,
    sdset_prefix: str | None = None,
    flipupdown: bool = False,
    skip_last: bool = False,
    show_fscolut: bool = False,
    help_flag: bool = False,
    help_full_flag: bool = False,
    flip_map_updside_down: bool = False,
    runner: Runner | None = None,
) -> MakeColorMapOutputs:
    """
    Utility for creating and modifying colormaps with various formats and fiducial
    points.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        fiducials_ncol: Fiducial colors and their indices in the color map are\
            listed in file Fiducials_Ncol.
        fiducials: Fiducial colors are listed in an ascii file Fiducials.
        num_colors: Total number of colors in the color map.
        std_mapname: Returns one of SUMA's standard colormaps.
        palette_file: Specify the palette file for colormap.
        cmap_name: Specify the colormap name.
        fscolut_labels: Get AFNI/SUMA colormaps of FreeSurfer colors indexed\
            between lbl0 and lbl1.
        fscolut_file: Use color LUT file FS_COL_LUT.
        afni_hex: Afni Hex format. Use this option if you want a color map\
            formatted to fit in AFNI's .afnirc file.
        afni_hex_complete: Afni Hex format, ready to go into pbardefs.h.
        suma_colormap: Write colormap in SUMA's format.
        user_colut_file: Provide a user's own color lookup file.
        sdset: Add colormap to surface-based dataset DSET, making it a labeled\
            dataset.
        sdset_prefix: Prefix of dset for writing labeled version of DSET.
        flipupdown: Flip the map upside down.
        skip_last: If used, the last color in the Fiducial list is omitted.
        show_fscolut: Show all of the FreeSurfer LUT.
        help_flag: Displays the help message.
        help_full_flag: Displays the help message.
        flip_map_updside_down: Flip the map upside down.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeColorMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_COLOR_MAP_METADATA)
    params = make_color_map_params(
        fiducials_ncol=fiducials_ncol,
        fiducials=fiducials,
        num_colors=num_colors,
        std_mapname=std_mapname,
        palette_file=palette_file,
        cmap_name=cmap_name,
        fscolut_labels=fscolut_labels,
        fscolut_file=fscolut_file,
        afni_hex=afni_hex,
        afni_hex_complete=afni_hex_complete,
        suma_colormap=suma_colormap,
        user_colut_file=user_colut_file,
        sdset=sdset,
        sdset_prefix=sdset_prefix,
        flipupdown=flipupdown,
        skip_last=skip_last,
        show_fscolut=show_fscolut,
        help_flag=help_flag,
        help_full_flag=help_full_flag,
        flip_map_updside_down=flip_map_updside_down,
    )
    return make_color_map_execute(params, execution)


__all__ = [
    "MAKE_COLOR_MAP_METADATA",
    "MakeColorMapOutputs",
    "MakeColorMapParameters",
    "make_color_map",
    "make_color_map_params",
]
