# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DMASK_TOOL_METADATA = Metadata(
    id="3803728aed061b1e42816745d337535ee20c4e5d.boutiques",
    name="3dmask_tool",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dmaskToolParameters = typing.TypedDict('V3dmaskToolParameters', {
    "__STYX_TYPE__": typing.Literal["3dmask_tool"],
    "count": bool,
    "datum": typing.NotRequired[typing.Literal["byte", "short", "float"] | None],
    "dilate_inputs": typing.NotRequired[str | None],
    "dilate_results": typing.NotRequired[str | None],
    "fill_dirs": typing.NotRequired[str | None],
    "fill_holes": bool,
    "frac": typing.NotRequired[float | None],
    "in_file": InputPathType,
    "inter": bool,
    "num_threads": typing.NotRequired[int | None],
    "outputtype": typing.NotRequired[typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None],
    "union": bool,
    "verbose": typing.NotRequired[int | None],
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
        "3dmask_tool": v_3dmask_tool_cargs,
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
        "3dmask_tool": v_3dmask_tool_outputs,
    }.get(t)


class V3dmaskToolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmask_tool(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Mask file."""


def v_3dmask_tool_params(
    in_file: InputPathType,
    count: bool = False,
    datum: typing.Literal["byte", "short", "float"] | None = None,
    dilate_inputs: str | None = None,
    dilate_results: str | None = None,
    fill_dirs: str | None = None,
    fill_holes: bool = False,
    frac: float | None = None,
    inter: bool = False,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    union: bool = False,
    verbose: int | None = None,
) -> V3dmaskToolParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input file to 3dmask_tool.
        count: Instead of created a binary 0/1 mask dataset, create one with\
            counts of voxel overlap, i.e., each voxel will contain the number of\
            masks that it is set in.
        datum: 'byte' or 'short' or 'float'. Specify data type for output.
        dilate_inputs: Use this option to dilate and/or erode datasets as they\
            are read. ex. '5 -5' to dilate and erode 5 times.
        dilate_results: Dilate and/or erode combined mask at the given levels.
        fill_dirs: Fill holes only in the given directions. this option is for\
            use with -fill holes. should be a single string that specifies 1-3 of\
            the axes using {x,y,z} labels (i.e. dataset axis order), or using the\
            labels in {r,l,a,p,i,s}.
        fill_holes: This option can be used to fill holes in the resulting\
            mask, i.e. after all other processing has been done.
        frac: When combining masks (across datasets and sub-bricks), use this\
            option to restrict the result to a certain fraction of the set of\
            volumes.
        inter: Intersection, this means -frac 1.0.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        union: Union, this means -frac 0.
        verbose: Specify verbosity level, for 0 to 3.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dmask_tool",
        "count": count,
        "fill_holes": fill_holes,
        "in_file": in_file,
        "inter": inter,
        "union": union,
    }
    if datum is not None:
        params["datum"] = datum
    if dilate_inputs is not None:
        params["dilate_inputs"] = dilate_inputs
    if dilate_results is not None:
        params["dilate_results"] = dilate_results
    if fill_dirs is not None:
        params["fill_dirs"] = fill_dirs
    if frac is not None:
        params["frac"] = frac
    if num_threads is not None:
        params["num_threads"] = num_threads
    if outputtype is not None:
        params["outputtype"] = outputtype
    if verbose is not None:
        params["verbose"] = verbose
    return params


def v_3dmask_tool_cargs(
    params: V3dmaskToolParameters,
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
    cargs.append("3dmask_tool")
    if params.get("count"):
        cargs.append("-count")
    if params.get("datum") is not None:
        cargs.extend([
            "-datum",
            params.get("datum")
        ])
    if params.get("dilate_inputs") is not None:
        cargs.extend([
            "-dilate_inputs",
            params.get("dilate_inputs")
        ])
    if params.get("dilate_results") is not None:
        cargs.extend([
            "-dilate_results",
            params.get("dilate_results")
        ])
    if params.get("fill_dirs") is not None:
        cargs.extend([
            "-fill_dirs",
            params.get("fill_dirs")
        ])
    if params.get("fill_holes"):
        cargs.append("-fill_holes")
    if params.get("frac") is not None:
        cargs.extend([
            "-frac",
            str(params.get("frac"))
        ])
    cargs.extend([
        "-input",
        execution.input_file(params.get("in_file"))
    ])
    if params.get("inter"):
        cargs.append("-inter")
    if params.get("num_threads") is not None:
        cargs.append(str(params.get("num_threads")))
    if params.get("outputtype") is not None:
        cargs.append(params.get("outputtype"))
    if params.get("union"):
        cargs.append("-union")
    if params.get("verbose") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbose"))
        ])
    return cargs


def v_3dmask_tool_outputs(
    params: V3dmaskToolParameters,
    execution: Execution,
) -> V3dmaskToolOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dmaskToolOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(params.get("in_file")).name + "_mask"),
        out_file_=execution.output_file("out_file"),
    )
    return ret


def v_3dmask_tool_execute(
    params: V3dmaskToolParameters,
    execution: Execution,
) -> V3dmaskToolOutputs:
    """
    3dmask_tool - for combining/dilating/eroding/filling masks.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dmaskToolOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dmask_tool_cargs(params, execution)
    ret = v_3dmask_tool_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dmask_tool(
    in_file: InputPathType,
    count: bool = False,
    datum: typing.Literal["byte", "short", "float"] | None = None,
    dilate_inputs: str | None = None,
    dilate_results: str | None = None,
    fill_dirs: str | None = None,
    fill_holes: bool = False,
    frac: float | None = None,
    inter: bool = False,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    union: bool = False,
    verbose: int | None = None,
    runner: Runner | None = None,
) -> V3dmaskToolOutputs:
    """
    3dmask_tool - for combining/dilating/eroding/filling masks.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input file to 3dmask_tool.
        count: Instead of created a binary 0/1 mask dataset, create one with\
            counts of voxel overlap, i.e., each voxel will contain the number of\
            masks that it is set in.
        datum: 'byte' or 'short' or 'float'. Specify data type for output.
        dilate_inputs: Use this option to dilate and/or erode datasets as they\
            are read. ex. '5 -5' to dilate and erode 5 times.
        dilate_results: Dilate and/or erode combined mask at the given levels.
        fill_dirs: Fill holes only in the given directions. this option is for\
            use with -fill holes. should be a single string that specifies 1-3 of\
            the axes using {x,y,z} labels (i.e. dataset axis order), or using the\
            labels in {r,l,a,p,i,s}.
        fill_holes: This option can be used to fill holes in the resulting\
            mask, i.e. after all other processing has been done.
        frac: When combining masks (across datasets and sub-bricks), use this\
            option to restrict the result to a certain fraction of the set of\
            volumes.
        inter: Intersection, this means -frac 1.0.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        union: Union, this means -frac 0.
        verbose: Specify verbosity level, for 0 to 3.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmaskToolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMASK_TOOL_METADATA)
    params = v_3dmask_tool_params(
        count=count,
        datum=datum,
        dilate_inputs=dilate_inputs,
        dilate_results=dilate_results,
        fill_dirs=fill_dirs,
        fill_holes=fill_holes,
        frac=frac,
        in_file=in_file,
        inter=inter,
        num_threads=num_threads,
        outputtype=outputtype,
        union=union,
        verbose=verbose,
    )
    return v_3dmask_tool_execute(params, execution)


__all__ = [
    "V3dmaskToolOutputs",
    "V3dmaskToolParameters",
    "V_3DMASK_TOOL_METADATA",
    "v_3dmask_tool",
    "v_3dmask_tool_params",
]
