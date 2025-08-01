# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_UNDUMP_METADATA = Metadata(
    id="a42a3e34bb6d7324060b71b7ded981c6489cdfe0.boutiques",
    name="3dUndump",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dUndumpParameters = typing.TypedDict('V3dUndumpParameters', {
    "__STYXTYPE__": typing.Literal["3dUndump"],
    "input_files": list[InputPathType],
    "prefix": typing.NotRequired[str | None],
    "master": typing.NotRequired[InputPathType | None],
    "dimensions": typing.NotRequired[list[float] | None],
    "mask": typing.NotRequired[InputPathType | None],
    "datatype": typing.NotRequired[str | None],
    "dval": typing.NotRequired[float | None],
    "fval": typing.NotRequired[float | None],
    "ijk": bool,
    "xyz": bool,
    "sphere_radius": typing.NotRequired[float | None],
    "cube_mode": bool,
    "orient": typing.NotRequired[str | None],
    "head_only": bool,
    "roimask": typing.NotRequired[InputPathType | None],
    "allow_nan": bool,
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
        "3dUndump": v_3d_undump_cargs,
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
        "3dUndump": v_3d_undump_outputs,
    }.get(t)


class V3dUndumpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_undump(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Main output dataset"""


def v_3d_undump_params(
    input_files: list[InputPathType],
    prefix: str | None = None,
    master: InputPathType | None = None,
    dimensions: list[float] | None = None,
    mask: InputPathType | None = None,
    datatype: str | None = None,
    dval: float | None = None,
    fval: float | None = None,
    ijk: bool = False,
    xyz: bool = False,
    sphere_radius: float | None = None,
    cube_mode: bool = False,
    orient: str | None = None,
    head_only: bool = False,
    roimask: InputPathType | None = None,
    allow_nan: bool = False,
) -> V3dUndumpParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input ASCII file(s), with one voxel specification per\
            line.
        prefix: 'ppp' is the prefix for the output dataset [default = undump].
        master: 'mmm' is the master dataset, whose geometry will determine the\
            geometry of the output.
        dimensions: Sets the dimensions of the output dataset to be I by J by K\
            voxels.
        mask: Specifies a mask dataset 'MMM', which will control which voxels\
            are allowed to get values set.
        datatype: 'type' determines the voxel data type of the output, which\
            may be byte, short, or float [default = short].
        dval: 'vvv' is the default value stored in each input voxel that does\
            not have a value supplied in the input file [default = 1].
        fval: 'fff' is the fill value, used for each voxel in the output\
            dataset that is NOT listed in the input file [default = 0].
        ijk: Coordinates in the input file are (i,j,k) index triples.
        xyz: Coordinates in the input file are (x,y,z) spatial coordinates, in\
            mm.
        sphere_radius: Specifies that a sphere of radius 'rrr' will be filled\
            about each input (x,y,z) or (i,j,k) voxel.
        cube_mode: Put cubes down instead of spheres. The 'radius' then is half\
            the length of a side.
        orient: Specifies the coordinate order used by -xyz. The code must be 3\
            letters, one each from the pairs {R,L} {A,P} {I,S}.
        head_only: Creates only the .HEAD file.
        roimask: Specifies which voxels get what numbers by using a dataset\
            'rrr', instead of coordinates.
        allow_nan: Allow NaN (not-a-number) values to be entered.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dUndump",
        "input_files": input_files,
        "ijk": ijk,
        "xyz": xyz,
        "cube_mode": cube_mode,
        "head_only": head_only,
        "allow_nan": allow_nan,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if master is not None:
        params["master"] = master
    if dimensions is not None:
        params["dimensions"] = dimensions
    if mask is not None:
        params["mask"] = mask
    if datatype is not None:
        params["datatype"] = datatype
    if dval is not None:
        params["dval"] = dval
    if fval is not None:
        params["fval"] = fval
    if sphere_radius is not None:
        params["sphere_radius"] = sphere_radius
    if orient is not None:
        params["orient"] = orient
    if roimask is not None:
        params["roimask"] = roimask
    return params


def v_3d_undump_cargs(
    params: V3dUndumpParameters,
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
    cargs.append("3dUndump")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("master") is not None:
        cargs.extend([
            "-master",
            execution.input_file(params.get("master"))
        ])
    if params.get("dimensions") is not None:
        cargs.extend([
            "-dimen",
            *map(str, params.get("dimensions"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("datatype") is not None:
        cargs.extend([
            "-datum",
            params.get("datatype")
        ])
    if params.get("dval") is not None:
        cargs.extend([
            "-dval",
            str(params.get("dval"))
        ])
    if params.get("fval") is not None:
        cargs.extend([
            "-fval",
            str(params.get("fval"))
        ])
    if params.get("ijk"):
        cargs.append("-ijk")
    if params.get("xyz"):
        cargs.append("-xyz")
    if params.get("sphere_radius") is not None:
        cargs.extend([
            "-srad",
            str(params.get("sphere_radius"))
        ])
    if params.get("cube_mode"):
        cargs.append("-cubes")
    if params.get("orient") is not None:
        cargs.extend([
            "-orient",
            params.get("orient")
        ])
    if params.get("head_only"):
        cargs.append("-head_only")
    if params.get("roimask") is not None:
        cargs.extend([
            "-ROImask",
            execution.input_file(params.get("roimask"))
        ])
    if params.get("allow_nan"):
        cargs.append("-allow_NaN")
    return cargs


def v_3d_undump_outputs(
    params: V3dUndumpParameters,
    execution: Execution,
) -> V3dUndumpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dUndumpOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("prefix") + ".nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_undump_execute(
    params: V3dUndumpParameters,
    execution: Execution,
) -> V3dUndumpOutputs:
    """
    Assembles a 3D dataset from an ASCII list of coordinates and optionally values.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dUndumpOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_undump_cargs(params, execution)
    ret = v_3d_undump_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_undump(
    input_files: list[InputPathType],
    prefix: str | None = None,
    master: InputPathType | None = None,
    dimensions: list[float] | None = None,
    mask: InputPathType | None = None,
    datatype: str | None = None,
    dval: float | None = None,
    fval: float | None = None,
    ijk: bool = False,
    xyz: bool = False,
    sphere_radius: float | None = None,
    cube_mode: bool = False,
    orient: str | None = None,
    head_only: bool = False,
    roimask: InputPathType | None = None,
    allow_nan: bool = False,
    runner: Runner | None = None,
) -> V3dUndumpOutputs:
    """
    Assembles a 3D dataset from an ASCII list of coordinates and optionally values.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input ASCII file(s), with one voxel specification per\
            line.
        prefix: 'ppp' is the prefix for the output dataset [default = undump].
        master: 'mmm' is the master dataset, whose geometry will determine the\
            geometry of the output.
        dimensions: Sets the dimensions of the output dataset to be I by J by K\
            voxels.
        mask: Specifies a mask dataset 'MMM', which will control which voxels\
            are allowed to get values set.
        datatype: 'type' determines the voxel data type of the output, which\
            may be byte, short, or float [default = short].
        dval: 'vvv' is the default value stored in each input voxel that does\
            not have a value supplied in the input file [default = 1].
        fval: 'fff' is the fill value, used for each voxel in the output\
            dataset that is NOT listed in the input file [default = 0].
        ijk: Coordinates in the input file are (i,j,k) index triples.
        xyz: Coordinates in the input file are (x,y,z) spatial coordinates, in\
            mm.
        sphere_radius: Specifies that a sphere of radius 'rrr' will be filled\
            about each input (x,y,z) or (i,j,k) voxel.
        cube_mode: Put cubes down instead of spheres. The 'radius' then is half\
            the length of a side.
        orient: Specifies the coordinate order used by -xyz. The code must be 3\
            letters, one each from the pairs {R,L} {A,P} {I,S}.
        head_only: Creates only the .HEAD file.
        roimask: Specifies which voxels get what numbers by using a dataset\
            'rrr', instead of coordinates.
        allow_nan: Allow NaN (not-a-number) values to be entered.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dUndumpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_UNDUMP_METADATA)
    params = v_3d_undump_params(
        input_files=input_files,
        prefix=prefix,
        master=master,
        dimensions=dimensions,
        mask=mask,
        datatype=datatype,
        dval=dval,
        fval=fval,
        ijk=ijk,
        xyz=xyz,
        sphere_radius=sphere_radius,
        cube_mode=cube_mode,
        orient=orient,
        head_only=head_only,
        roimask=roimask,
        allow_nan=allow_nan,
    )
    return v_3d_undump_execute(params, execution)


__all__ = [
    "V3dUndumpOutputs",
    "V3dUndumpParameters",
    "V_3D_UNDUMP_METADATA",
    "v_3d_undump",
    "v_3d_undump_params",
]
