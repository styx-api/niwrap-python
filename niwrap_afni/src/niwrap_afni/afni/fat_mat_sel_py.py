# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FAT_MAT_SEL_PY_METADATA = Metadata(
    id="88fca2178c80442aa63260a3d75da0e0c0b65a59.boutiques",
    name="fat_mat_sel.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


FatMatSelPyParameters = typing.TypedDict('FatMatSelPyParameters', {
    "__STYXTYPE__": typing.Literal["fat_mat_sel.py"],
    "parameters": str,
    "matr_in": typing.NotRequired[str | None],
    "list_match": typing.NotRequired[InputPathType | None],
    "out_ind_matr": bool,
    "out_ind_1ddset": bool,
    "hold_image": bool,
    "extern_labs_no": bool,
    "type_file": typing.NotRequired[str | None],
    "dpi_file": typing.NotRequired[float | None],
    "xlen_file": typing.NotRequired[float | None],
    "ylen_file": typing.NotRequired[float | None],
    "tight_layout_on": bool,
    "fig_off": bool,
    "size_font": typing.NotRequired[float | None],
    "lab_size_font": typing.NotRequired[float | None],
    "a_plotmin": typing.NotRequired[float | None],
    "b_plotmax": typing.NotRequired[float | None],
    "cbar_off": bool,
    "map_of_colors": typing.NotRequired[str | None],
    "cbar_int_num": typing.NotRequired[float | None],
    "width_cbar_perc": typing.NotRequired[float | None],
    "specifier": typing.NotRequired[str | None],
    "xtick_lab_off": bool,
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
        "fat_mat_sel.py": fat_mat_sel_py_cargs,
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
        "fat_mat_sel.py": fat_mat_sel_py_outputs,
    }.get(t)


class FatMatSelPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_mat_sel_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    individual_images: OutputPathType
    """Individual images of matrix plots."""
    matrix_grids: OutputPathType
    """Output matrix grid files."""
    v_1_d_dsets: OutputPathType
    """Output 1D dataset files."""


def fat_mat_sel_py_params(
    parameters: str,
    matr_in: str | None = None,
    list_match: InputPathType | None = None,
    out_ind_matr: bool = False,
    out_ind_1ddset: bool = False,
    hold_image: bool = False,
    extern_labs_no: bool = False,
    type_file: str | None = None,
    dpi_file: float | None = None,
    xlen_file: float | None = None,
    ylen_file: float | None = None,
    tight_layout_on: bool = False,
    fig_off: bool = False,
    size_font: float | None = None,
    lab_size_font: float | None = None,
    a_plotmin: float | None = None,
    b_plotmax: float | None = None,
    cbar_off: bool = False,
    map_of_colors: str | None = None,
    cbar_int_num: float | None = None,
    width_cbar_perc: float | None = None,
    specifier: str | None = None,
    xtick_lab_off: bool = False,
) -> FatMatSelPyParameters:
    """
    Build parameters.
    
    Args:
        parameters: Supply names of parameters, separated by whitespace, for\
            selecting from a matrix file.
        matr_in: Provide the set of matrix (*.grid or *.netcc) files by\
            searchable path. This can be a globbable entry in quotes containing\
            wildcard characters.
        list_match: Provide the matrix (*.grid or *.netcc) files by explicit\
            path, matched per file with a CSV subject ID.
        out_ind_matr: Output individual matrix files of properties.
        out_ind_1ddset: Output as a 1D dset, more easily readable by other\
            programs.
        hold_image: Switch to hold the Python-produced image on the output\
            screen until a key has been hit.
        extern_labs_no: Switch to turn off the usage of user-defined labels in\
            the *.grid/*.netcc files.
        type_file: Select image format type (e.g., jpg, png, pdf).
        dpi_file: Set resolution (dots per inch) of output image.
        xlen_file: Horizontal dimension of output saved image, in units of\
            inches.
        ylen_file: Vertical dimension of output saved image, in units of\
            inches.
        tight_layout_on: Use matplotlib's tight_layout() option to ensure no\
            overlap of features in the image.
        fig_off: Switch if you don't want matrix figure output.
        size_font: Set font size for colorbar and title.
        lab_size_font: Set font size for x- and y-axis labels.
        a_plotmin: Minimum colorbar value.
        b_plotmax: Maximum colorbar value.
        cbar_off: Switch to not include a colorbar at the right side of the\
            plot.
        map_of_colors: Change the colormap style used in the plot.
        cbar_int_num: Set the number of intervals on the colorbar.
        width_cbar_perc: Width of colorbar as percentage of width of the\
            correlation matrix.
        specifier: Specify number formatting for the colorbar numbers (e.g.,\
            '%.4f' for four decimal places).
        xtick_lab_off: Switch to turn off labels along the x- (horizontal) axis\
            but leave those along the y- (vertical) axis.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_mat_sel.py",
        "parameters": parameters,
        "out_ind_matr": out_ind_matr,
        "out_ind_1ddset": out_ind_1ddset,
        "hold_image": hold_image,
        "extern_labs_no": extern_labs_no,
        "tight_layout_on": tight_layout_on,
        "fig_off": fig_off,
        "cbar_off": cbar_off,
        "xtick_lab_off": xtick_lab_off,
    }
    if matr_in is not None:
        params["matr_in"] = matr_in
    if list_match is not None:
        params["list_match"] = list_match
    if type_file is not None:
        params["type_file"] = type_file
    if dpi_file is not None:
        params["dpi_file"] = dpi_file
    if xlen_file is not None:
        params["xlen_file"] = xlen_file
    if ylen_file is not None:
        params["ylen_file"] = ylen_file
    if size_font is not None:
        params["size_font"] = size_font
    if lab_size_font is not None:
        params["lab_size_font"] = lab_size_font
    if a_plotmin is not None:
        params["a_plotmin"] = a_plotmin
    if b_plotmax is not None:
        params["b_plotmax"] = b_plotmax
    if map_of_colors is not None:
        params["map_of_colors"] = map_of_colors
    if cbar_int_num is not None:
        params["cbar_int_num"] = cbar_int_num
    if width_cbar_perc is not None:
        params["width_cbar_perc"] = width_cbar_perc
    if specifier is not None:
        params["specifier"] = specifier
    return params


def fat_mat_sel_py_cargs(
    params: FatMatSelPyParameters,
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
    cargs.append("fat_mat_sel.py")
    cargs.extend([
        "--Pars",
        params.get("parameters")
    ])
    if params.get("matr_in") is not None:
        cargs.extend([
            "--matr_in",
            params.get("matr_in")
        ])
    if params.get("list_match") is not None:
        cargs.extend([
            "--list_match",
            execution.input_file(params.get("list_match"))
        ])
    if params.get("out_ind_matr"):
        cargs.append("--out_ind_matr")
    if params.get("out_ind_1ddset"):
        cargs.append("--Out_ind_1ddset")
    if params.get("hold_image"):
        cargs.append("--Hold_image")
    if params.get("extern_labs_no"):
        cargs.append("--ExternLabsNo")
    if params.get("type_file") is not None:
        cargs.extend([
            "--type_file",
            params.get("type_file")
        ])
    if params.get("dpi_file") is not None:
        cargs.extend([
            "--dpi_file",
            str(params.get("dpi_file"))
        ])
    if params.get("xlen_file") is not None:
        cargs.extend([
            "--xlen_file",
            str(params.get("xlen_file"))
        ])
    if params.get("ylen_file") is not None:
        cargs.extend([
            "--ylen_file",
            str(params.get("ylen_file"))
        ])
    if params.get("tight_layout_on"):
        cargs.append("--Tight_layout_on")
    if params.get("fig_off"):
        cargs.append("--Fig_off")
    if params.get("size_font") is not None:
        cargs.extend([
            "--Size_font",
            str(params.get("size_font"))
        ])
    if params.get("lab_size_font") is not None:
        cargs.extend([
            "--Lab_size_font",
            str(params.get("lab_size_font"))
        ])
    if params.get("a_plotmin") is not None:
        cargs.extend([
            "--A_plotmin",
            str(params.get("a_plotmin"))
        ])
    if params.get("b_plotmax") is not None:
        cargs.extend([
            "--B_plotmax",
            str(params.get("b_plotmax"))
        ])
    if params.get("cbar_off"):
        cargs.append("--Cbar_off")
    if params.get("map_of_colors") is not None:
        cargs.extend([
            "--Map_of_colors",
            params.get("map_of_colors")
        ])
    if params.get("cbar_int_num") is not None:
        cargs.extend([
            "--cbar_int_num",
            str(params.get("cbar_int_num"))
        ])
    if params.get("width_cbar_perc") is not None:
        cargs.extend([
            "--width_cbar_perc",
            str(params.get("width_cbar_perc"))
        ])
    if params.get("specifier") is not None:
        cargs.extend([
            "--specifier",
            params.get("specifier")
        ])
    if params.get("xtick_lab_off"):
        cargs.append("--Xtick_lab_off")
    return cargs


def fat_mat_sel_py_outputs(
    params: FatMatSelPyParameters,
    execution: Execution,
) -> FatMatSelPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatMatSelPyOutputs(
        root=execution.output_file("."),
        individual_images=execution.output_file("individual_images/*"),
        matrix_grids=execution.output_file("matrix_grids/*"),
        v_1_d_dsets=execution.output_file("1D_dsets/*"),
    )
    return ret


def fat_mat_sel_py_execute(
    params: FatMatSelPyParameters,
    execution: Execution,
) -> FatMatSelPyOutputs:
    """
    Perform simple matrix plotting operations from outputs of FATCAT programs
    3dNetCorr and 3dTrackID.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatMatSelPyOutputs`).
    """
    params = execution.params(params)
    cargs = fat_mat_sel_py_cargs(params, execution)
    ret = fat_mat_sel_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def fat_mat_sel_py(
    parameters: str,
    matr_in: str | None = None,
    list_match: InputPathType | None = None,
    out_ind_matr: bool = False,
    out_ind_1ddset: bool = False,
    hold_image: bool = False,
    extern_labs_no: bool = False,
    type_file: str | None = None,
    dpi_file: float | None = None,
    xlen_file: float | None = None,
    ylen_file: float | None = None,
    tight_layout_on: bool = False,
    fig_off: bool = False,
    size_font: float | None = None,
    lab_size_font: float | None = None,
    a_plotmin: float | None = None,
    b_plotmax: float | None = None,
    cbar_off: bool = False,
    map_of_colors: str | None = None,
    cbar_int_num: float | None = None,
    width_cbar_perc: float | None = None,
    specifier: str | None = None,
    xtick_lab_off: bool = False,
    runner: Runner | None = None,
) -> FatMatSelPyOutputs:
    """
    Perform simple matrix plotting operations from outputs of FATCAT programs
    3dNetCorr and 3dTrackID.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        parameters: Supply names of parameters, separated by whitespace, for\
            selecting from a matrix file.
        matr_in: Provide the set of matrix (*.grid or *.netcc) files by\
            searchable path. This can be a globbable entry in quotes containing\
            wildcard characters.
        list_match: Provide the matrix (*.grid or *.netcc) files by explicit\
            path, matched per file with a CSV subject ID.
        out_ind_matr: Output individual matrix files of properties.
        out_ind_1ddset: Output as a 1D dset, more easily readable by other\
            programs.
        hold_image: Switch to hold the Python-produced image on the output\
            screen until a key has been hit.
        extern_labs_no: Switch to turn off the usage of user-defined labels in\
            the *.grid/*.netcc files.
        type_file: Select image format type (e.g., jpg, png, pdf).
        dpi_file: Set resolution (dots per inch) of output image.
        xlen_file: Horizontal dimension of output saved image, in units of\
            inches.
        ylen_file: Vertical dimension of output saved image, in units of\
            inches.
        tight_layout_on: Use matplotlib's tight_layout() option to ensure no\
            overlap of features in the image.
        fig_off: Switch if you don't want matrix figure output.
        size_font: Set font size for colorbar and title.
        lab_size_font: Set font size for x- and y-axis labels.
        a_plotmin: Minimum colorbar value.
        b_plotmax: Maximum colorbar value.
        cbar_off: Switch to not include a colorbar at the right side of the\
            plot.
        map_of_colors: Change the colormap style used in the plot.
        cbar_int_num: Set the number of intervals on the colorbar.
        width_cbar_perc: Width of colorbar as percentage of width of the\
            correlation matrix.
        specifier: Specify number formatting for the colorbar numbers (e.g.,\
            '%.4f' for four decimal places).
        xtick_lab_off: Switch to turn off labels along the x- (horizontal) axis\
            but leave those along the y- (vertical) axis.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatMatSelPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_MAT_SEL_PY_METADATA)
    params = fat_mat_sel_py_params(
        parameters=parameters,
        matr_in=matr_in,
        list_match=list_match,
        out_ind_matr=out_ind_matr,
        out_ind_1ddset=out_ind_1ddset,
        hold_image=hold_image,
        extern_labs_no=extern_labs_no,
        type_file=type_file,
        dpi_file=dpi_file,
        xlen_file=xlen_file,
        ylen_file=ylen_file,
        tight_layout_on=tight_layout_on,
        fig_off=fig_off,
        size_font=size_font,
        lab_size_font=lab_size_font,
        a_plotmin=a_plotmin,
        b_plotmax=b_plotmax,
        cbar_off=cbar_off,
        map_of_colors=map_of_colors,
        cbar_int_num=cbar_int_num,
        width_cbar_perc=width_cbar_perc,
        specifier=specifier,
        xtick_lab_off=xtick_lab_off,
    )
    return fat_mat_sel_py_execute(params, execution)


__all__ = [
    "FAT_MAT_SEL_PY_METADATA",
    "FatMatSelPyOutputs",
    "FatMatSelPyParameters",
    "fat_mat_sel_py",
    "fat_mat_sel_py_params",
]
