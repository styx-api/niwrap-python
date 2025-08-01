# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DREFIT_METADATA = Metadata(
    id="3f540f91056434ebd87b76f91b70964cf1dec091.boutiques",
    name="3drefit",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3drefitParameters = typing.TypedDict('V3drefitParameters', {
    "__STYXTYPE__": typing.Literal["3drefit"],
    "atrcopy": typing.NotRequired[list[str] | None],
    "atrfloat": typing.NotRequired[list[str] | None],
    "atrint": typing.NotRequired[list[str] | None],
    "atrstring": typing.NotRequired[list[str] | None],
    "deoblique": bool,
    "duporigin_file": typing.NotRequired[InputPathType | None],
    "in_file": InputPathType,
    "nosaveatr": bool,
    "saveatr": bool,
    "space": typing.NotRequired[typing.Literal["TLRC", "MNI", "ORIG"] | None],
    "xdel": typing.NotRequired[float | None],
    "xorigin": typing.NotRequired[str | None],
    "xyzscale": typing.NotRequired[float | None],
    "ydel": typing.NotRequired[float | None],
    "yorigin": typing.NotRequired[str | None],
    "zdel": typing.NotRequired[float | None],
    "zorigin": typing.NotRequired[str | None],
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
        "3drefit": v_3drefit_cargs,
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
        "3drefit": v_3drefit_outputs,
    }.get(t)


class V3drefitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3drefit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output file."""


def v_3drefit_params(
    in_file: InputPathType,
    atrcopy: list[str] | None = None,
    atrfloat: list[str] | None = None,
    atrint: list[str] | None = None,
    atrstring: list[str] | None = None,
    deoblique: bool = False,
    duporigin_file: InputPathType | None = None,
    nosaveatr: bool = False,
    saveatr: bool = False,
    space: typing.Literal["TLRC", "MNI", "ORIG"] | None = None,
    xdel: float | None = None,
    xorigin: str | None = None,
    xyzscale: float | None = None,
    ydel: float | None = None,
    yorigin: str | None = None,
    zdel: float | None = None,
    zorigin: str | None = None,
) -> V3drefitParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input file to 3drefit.
        atrcopy: (file, string). Copy afni header attribute from the given file\
            into the header of the dataset(s) being modified. for more information\
            on afni header attributes, see documentation file readme.attributes.\
            more than one '-atrcopy' option can be used. for afni advanced users\
            only. do not use -atrcopy or -atrstring with other modification\
            options. see also -copyaux.
        atrfloat: (a string, a string). Create or modify floating point\
            attributes. the input values may be specified as a single string in\
            quotes or as a 1d filename or string, example '1 0.2 0 0 -0.2 1 0 0 0 0\
            1 0' or flipz.1d or '1d:1,0.2,2@0,-0.2,1,2@0,2@0,1,0'.
        atrint: (a string, a string). Create or modify integer attributes. the\
            input values may be specified as a single string in quotes or as a 1d\
            filename or string, example '1 0 0 0 0 1 0 0 0 0 1 0' or flipz.1d or\
            '1d:1,0,2@0,-0,1,2@0,2@0,1,0'.
        atrstring: (a string, a string). Copy the last given string into the\
            dataset(s) being modified, giving it the attribute name given by the\
            last string.to be safe, the last string should be in quotes.
        deoblique: Replace current transformation matrix with cardinal matrix.
        duporigin_file: Copies the xorigin, yorigin, and zorigin values from\
            the header of the given dataset.
        nosaveatr: Opposite of -saveatr.
        saveatr: (default) copy the attributes that are known to afni into the\
            dset->dblk structure thereby forcing changes to known attributes to be\
            present in the output. this option only makes sense with -atrcopy.
        space: 'tlrc' or 'mni' or 'orig'. Associates the dataset with a\
            specific template type, e.g. tlrc, mni, orig.
        xdel: New x voxel dimension in mm.
        xorigin: X distance for edge voxel offset.
        xyzscale: Scale the size of the dataset voxels by the given factor.
        ydel: New y voxel dimension in mm.
        yorigin: Y distance for edge voxel offset.
        zdel: New z voxel dimension in mm.
        zorigin: Z distance for edge voxel offset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3drefit",
        "deoblique": deoblique,
        "in_file": in_file,
        "nosaveatr": nosaveatr,
        "saveatr": saveatr,
    }
    if atrcopy is not None:
        params["atrcopy"] = atrcopy
    if atrfloat is not None:
        params["atrfloat"] = atrfloat
    if atrint is not None:
        params["atrint"] = atrint
    if atrstring is not None:
        params["atrstring"] = atrstring
    if duporigin_file is not None:
        params["duporigin_file"] = duporigin_file
    if space is not None:
        params["space"] = space
    if xdel is not None:
        params["xdel"] = xdel
    if xorigin is not None:
        params["xorigin"] = xorigin
    if xyzscale is not None:
        params["xyzscale"] = xyzscale
    if ydel is not None:
        params["ydel"] = ydel
    if yorigin is not None:
        params["yorigin"] = yorigin
    if zdel is not None:
        params["zdel"] = zdel
    if zorigin is not None:
        params["zorigin"] = zorigin
    return params


def v_3drefit_cargs(
    params: V3drefitParameters,
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
    cargs.append("3drefit")
    if params.get("atrcopy") is not None:
        cargs.extend([
            "-atrcopy",
            *params.get("atrcopy")
        ])
    if params.get("atrfloat") is not None:
        cargs.extend([
            "-atrfloat",
            *params.get("atrfloat")
        ])
    if params.get("atrint") is not None:
        cargs.extend([
            "-atrint",
            *params.get("atrint")
        ])
    if params.get("atrstring") is not None:
        cargs.extend([
            "-atrstring",
            *params.get("atrstring")
        ])
    if params.get("deoblique"):
        cargs.append("-deoblique")
    if params.get("duporigin_file") is not None:
        cargs.extend([
            "-duporigin",
            execution.input_file(params.get("duporigin_file"))
        ])
    cargs.append(execution.input_file(params.get("in_file"), mutable=True))
    if params.get("nosaveatr"):
        cargs.append("-nosaveatr")
    if params.get("saveatr"):
        cargs.append("-saveatr")
    if params.get("space") is not None:
        cargs.extend([
            "-space",
            params.get("space")
        ])
    if params.get("xdel") is not None:
        cargs.extend([
            "-xdel",
            str(params.get("xdel"))
        ])
    if params.get("xorigin") is not None:
        cargs.extend([
            "-xorigin",
            params.get("xorigin")
        ])
    if params.get("xyzscale") is not None:
        cargs.extend([
            "-xyzscale",
            str(params.get("xyzscale"))
        ])
    if params.get("ydel") is not None:
        cargs.extend([
            "-ydel",
            str(params.get("ydel"))
        ])
    if params.get("yorigin") is not None:
        cargs.extend([
            "-yorigin",
            params.get("yorigin")
        ])
    if params.get("zdel") is not None:
        cargs.extend([
            "-zdel",
            str(params.get("zdel"))
        ])
    if params.get("zorigin") is not None:
        cargs.extend([
            "-zorigin",
            params.get("zorigin")
        ])
    return cargs


def v_3drefit_outputs(
    params: V3drefitParameters,
    execution: Execution,
) -> V3drefitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3drefitOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file("out_file"),
    )
    return ret


def v_3drefit_execute(
    params: V3drefitParameters,
    execution: Execution,
) -> V3drefitOutputs:
    """
    Changes some of the information inside a 3D dataset's header.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3drefitOutputs`).
    """
    params = execution.params(params)
    cargs = v_3drefit_cargs(params, execution)
    ret = v_3drefit_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3drefit(
    in_file: InputPathType,
    atrcopy: list[str] | None = None,
    atrfloat: list[str] | None = None,
    atrint: list[str] | None = None,
    atrstring: list[str] | None = None,
    deoblique: bool = False,
    duporigin_file: InputPathType | None = None,
    nosaveatr: bool = False,
    saveatr: bool = False,
    space: typing.Literal["TLRC", "MNI", "ORIG"] | None = None,
    xdel: float | None = None,
    xorigin: str | None = None,
    xyzscale: float | None = None,
    ydel: float | None = None,
    yorigin: str | None = None,
    zdel: float | None = None,
    zorigin: str | None = None,
    runner: Runner | None = None,
) -> V3drefitOutputs:
    """
    Changes some of the information inside a 3D dataset's header.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input file to 3drefit.
        atrcopy: (file, string). Copy afni header attribute from the given file\
            into the header of the dataset(s) being modified. for more information\
            on afni header attributes, see documentation file readme.attributes.\
            more than one '-atrcopy' option can be used. for afni advanced users\
            only. do not use -atrcopy or -atrstring with other modification\
            options. see also -copyaux.
        atrfloat: (a string, a string). Create or modify floating point\
            attributes. the input values may be specified as a single string in\
            quotes or as a 1d filename or string, example '1 0.2 0 0 -0.2 1 0 0 0 0\
            1 0' or flipz.1d or '1d:1,0.2,2@0,-0.2,1,2@0,2@0,1,0'.
        atrint: (a string, a string). Create or modify integer attributes. the\
            input values may be specified as a single string in quotes or as a 1d\
            filename or string, example '1 0 0 0 0 1 0 0 0 0 1 0' or flipz.1d or\
            '1d:1,0,2@0,-0,1,2@0,2@0,1,0'.
        atrstring: (a string, a string). Copy the last given string into the\
            dataset(s) being modified, giving it the attribute name given by the\
            last string.to be safe, the last string should be in quotes.
        deoblique: Replace current transformation matrix with cardinal matrix.
        duporigin_file: Copies the xorigin, yorigin, and zorigin values from\
            the header of the given dataset.
        nosaveatr: Opposite of -saveatr.
        saveatr: (default) copy the attributes that are known to afni into the\
            dset->dblk structure thereby forcing changes to known attributes to be\
            present in the output. this option only makes sense with -atrcopy.
        space: 'tlrc' or 'mni' or 'orig'. Associates the dataset with a\
            specific template type, e.g. tlrc, mni, orig.
        xdel: New x voxel dimension in mm.
        xorigin: X distance for edge voxel offset.
        xyzscale: Scale the size of the dataset voxels by the given factor.
        ydel: New y voxel dimension in mm.
        yorigin: Y distance for edge voxel offset.
        zdel: New z voxel dimension in mm.
        zorigin: Z distance for edge voxel offset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3drefitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DREFIT_METADATA)
    params = v_3drefit_params(
        atrcopy=atrcopy,
        atrfloat=atrfloat,
        atrint=atrint,
        atrstring=atrstring,
        deoblique=deoblique,
        duporigin_file=duporigin_file,
        in_file=in_file,
        nosaveatr=nosaveatr,
        saveatr=saveatr,
        space=space,
        xdel=xdel,
        xorigin=xorigin,
        xyzscale=xyzscale,
        ydel=ydel,
        yorigin=yorigin,
        zdel=zdel,
        zorigin=zorigin,
    )
    return v_3drefit_execute(params, execution)


__all__ = [
    "V3drefitOutputs",
    "V3drefitParameters",
    "V_3DREFIT_METADATA",
    "v_3drefit",
    "v_3drefit_params",
]
